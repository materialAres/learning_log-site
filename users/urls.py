"""URL patterns for users"""

from django.urls import path, include
from . import views


app_name = 'users'


urlpatterns = [
    # A set of authentication urls provided into django
    path('', include('django.contrib.auth.urls')), # This URL includes useful URLs patterns for the authentication process, like login and logout, ready to be used saving us the time to create them one by one.
                                                  # N.B. When we write a URL like localhost/users/login, the word 'users' makes django search in urls.py for a match, and 'login' sends a request to the default *login* view function already implemented in django.
    path('register/', views.register, name='register')
]

