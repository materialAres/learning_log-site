"""View functions allow us to send data from a database to a template, and show it in web pages, with a series of functionalities that we choose.
Filly, through them we send an http request and we receive a response."""

from django.shortcuts import render, redirect, get_object_or_404   # redirect allows the program to redirect to another page/url, in this case it redirects the user from the topic-submission page to the topics page.
from django.contrib.auth.decorators import login_required
from .models import Entry, Topic
from .forms import TopicForm, EntryForm
from django.http import Http404


# Check whether the user is the owner of the topic, raise an error instead
def check_topic_owner(owner, user):
    if owner != user:
        raise Http404


# Create your views here.
def index(request):
    """Learning log's Home Page"""
    return render(request, 'learning_logs/index.html')


@login_required     # Decorators modify the behaviour of a function (or a class), modifying its functionalities; we basically wrap the function (la avvolgiamo) with another function
def topics(request):
    """Topic's page"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')    # Filter allows only the user to see its own data, but it's not enough, we need to raise an error if s1 tries to enter the topic of another user
    context = {'topics': topics} # Dictionary of data to send to the template; the key is the name we'll use to access the data, and the value is the data itself
    return render(request, 'learning_logs/topics.html', context) # Combine a template and a dictionary (context)


@login_required
def topic(request, topic_id):
    """Show a single topic and its entries"""
    topic = get_object_or_404(Topic, id=topic_id)

    check_topic_owner(topic.owner, request.user)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        form = TopicForm() # No data submitted, create a blank page
    else:
        form = TopicForm(data=request.POST) # POST is a request that allows users to submit information in a web page; GET is used to read data from a server.
        if form.is_valid():
            new_topic = form.save(commit=False)     # with 'commit' we are not immediately saving the topic into the database, so we can make further actions
            new_topic.owner = request.user          # WHAT this 'request' do actually?
            new_topic.save()
            return redirect('learning_logs:topics')     # redirect the user to the view 'learning....'.
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a topic."""
    topic = Topic.objects.get(id=topic_id)

    check_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic 
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id) # At the end, redirect the user to another url (in this case 'topic'). IMPORTANT: the url must exist in your urls.py section (obv :D)!

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)  

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    check_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        form = EntryForm(instance=entry)    # Initial request; the form is filled with the existing entry we have precedently made
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
     