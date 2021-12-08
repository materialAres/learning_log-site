from django.contrib import admin

from learning_logs.models import Topic, Entry, ToDo

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(ToDo)
