from django.db import models
from forum.models.forum import Forum


class Discussion(models.Model):
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.forum)
