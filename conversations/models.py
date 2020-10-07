from django.conf import settings
from django.db import models
from core.models import AbstractTimestamp


class Conversation(AbstractTimestamp):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="conversation")

    def __str__(self):
        return str(self.created)

    def count_messages(self):
        return self.messages.count()
    
    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()
    
    count_participants.short_description = "Number of Participants"


class Message(AbstractTimestamp):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="messages")
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")

    def __str__(self):
        usernames = []
        for user in self.conversation.all():
            usernames.append(user.username)
        return ", ".join(usernames)
