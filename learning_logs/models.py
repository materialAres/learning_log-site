"""A model tells D how to work with the data we import in the app; it is a class in fact."""

from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Topic(models.Model):
    """Topic the user is learning"""
    text = models.CharField(max_length=200) #Allows to store a small text; see p289 to look to every fields you can use in model
    date_added = models.DateTimeField(auto_now_add=True) #create a variable which expresses the time the topic is created; auto_now_add automatically sets the attribute to the current real time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """What we specifically learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the model"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
            