from django.contrib.auth import login
from django.views.generic import FormView

from authentication.forms import LoginForm, RegistrationForm
from authentication.models import User


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.user)
        return super().form_valid(form)


class RegistrationView(FormView):
    template_name = "register.html"
    form_class = RegistrationForm

    def form_valid(self, form):
        user = User(username=form.username, password=form.password)
        return super().form_valid(form)
