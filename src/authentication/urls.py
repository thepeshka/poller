from django.urls import path

from authentication.views import LoginView, RegistrationView, LogoutView

app_name = "authentication"

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('register', RegistrationView.as_view(), name="register"),
    path('logout', LogoutView.as_view(), name="logout")
]
