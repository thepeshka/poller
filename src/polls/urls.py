from django.urls import path

from polls.views import HomeView

urlpatterns = [
    path('/', HomeView.as_view()),
]
