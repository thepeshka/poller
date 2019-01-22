from django.urls import path

from polls.views import HomeView

app_name = "polls"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]
