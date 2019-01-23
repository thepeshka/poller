from django.db.models import *


class Poll(Model):
    name = CharField(max_length=50)
    description = TextField()
    multiple_answers = BooleanField(default=False)



class PollAnswer(Model):
    poll = ForeignKey(Poll, on_delete=CASCADE, related_name="answer")
    title = CharField(max_length=50)
