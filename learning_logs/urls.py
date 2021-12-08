"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Topic's page
    path('topics/', views.topics, name='topics'), # In the first argument of path, we specify the name the url has

    # Single topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Topic added by an user
    path('new_topic/', views.new_topic, name='new_topic'),

    # Entry added by an user
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Edit an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # Create a new ToDo
    path('new_todo/<int:topic_id>/', views.new_todo, name='new_todo'),
]
