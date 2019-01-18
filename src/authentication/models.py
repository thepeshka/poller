from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    real_name = CharField(max_length=50)
