from django.db.models import Model, CharField


class Poll(Model):
    name = CharField(max_length=50)
