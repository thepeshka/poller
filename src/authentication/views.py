from django.contrib.auth import login
from django.views.generic import FormView

from authentication.forms import LoginForm


class LoginView(FormView):
    template_name = "login_view.html"
    form_class = LoginForm

    def form_valid(self, form):
        login(self.request, form.user)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        return context