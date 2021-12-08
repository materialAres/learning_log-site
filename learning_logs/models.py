"""A model tells Django how to work with the data we import in the app; it is a class in fact."""

import datetime

from typing import Text
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


def past_or_future_date(date):
    """We use this function in our ToDo model, to ensure that a user cannot insert
    a date minor to the day they creates the new to do."""
    if date < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return date


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


class ToDo(models.Model):
    """What we will learn in the future about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, editable=False)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField("Due date (The date must be in the format MM/DD/YYYY)", validators=[past_or_future_date])

    class Meta:
            verbose_name_plural = "todos"

    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
            