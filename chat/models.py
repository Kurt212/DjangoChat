from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ChatMessage(models.Model):
    room = models.CharField(max_length=100, blank=False)
    text = models.TextField(blank=False)
    
    time_created = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,)

    def __str__(self):
        if self.author is None:
            name = "Unknown"
        else:
            name = self.author.username 
        return "(room={0}, text={1}, time_created={2}, author={3})".format(self.room, self.text, self.time_created, name)

    def to_text(self):
        time = timezone.localtime(self.time_created)
        if self.author is None:
            return "[{0}][Unknown]: {1}".format(time.strftime("%H:%M"), self.text)
        else:
            return "[{0}][{1}]: {2}".format(time.strftime("%H:%M"), self.author.username, self.text)
