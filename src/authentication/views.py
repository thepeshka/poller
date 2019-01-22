from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
from django.conf import settings

from authentication.forms import LoginForm, RegistrationForm
from authentication.models import User


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def get_success_url(self):
        return reverse("polls:home")

    def form_valid(self, form):
        login(self.request, form.user)
        return super().form_valid(form)


class RegistrationView(FormView):
    template_name = "register.html"
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse("polls:home")

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse("polls.home"))
        elif settings.REGISTRATION_IS_OPEN or self.request.GET.get("secret") == settings.REGISTRATION_SECRET:
            return super().get(self, *args, **kwargs)
        else:
            return redirect(reverse("polls:home") + "?alert=registration_closed")

    def form_valid(self, form):
        user = User(username=form.username, password=form.password)
        user.save()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect(reverse("polls:home"))
