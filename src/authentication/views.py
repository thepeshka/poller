from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import FormView
from django.conf import settings

from authentication.forms import LoginForm, RegistrationForm
from authentication.models import User


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        login(self.request, form.user)
        return super().form_valid(form)


class RegistrationView(FormView):
    template_name = "register.html"
    form_class = RegistrationForm
    success_url = "/"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/")
        elif settings.REGISTRATION_IS_OPEN or self.request.GET.get("secret") == settings.REGISTRATION_SECRET:
            return super().get(self, *args, **kwargs)
        else:
            return redirect("/?alert=registration_closed")

    def form_valid(self, form):
        user = User(username=form.username, password=form.password)
        user.save()
        login(self.request, user)
        return super().form_valid(form)
