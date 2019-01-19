from django.contrib.auth import login
from django.views.generic import FormView

from authentication.forms import LoginForm, RegistrationForm


class LoginView(FormView):
    template_name = "login_view.html"
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.user)
        return super().form_valid(form)


class RegistrationView(FormView):
    template_name = "login_view.html"
    form_class = RegistrationForm

    def form_valid(self, form):
        return super().form_valid(form)
