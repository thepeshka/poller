from django.urls import path

from authentication.views import LoginView, RegistrationView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegistrationView.as_view())
]
