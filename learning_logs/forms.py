from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Topic, Entry, ToDo


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text':forms.Textarea(attrs={'rows': 6, 'cols':80})} # Override Django default widget of text area, giving more space to write increasing columns value from 40 to 80.


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['text', 'due_date']
        labels = {'todo': '', 'due date': ''}
        widgets = {'text':forms.Textarea(attrs={'rows':2, 'cols':20})}
