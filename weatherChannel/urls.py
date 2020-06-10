from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

# This syntax imports all of the functions and classes
# inside the views.py in the same folder.
from . import views
urlpatterns = [
    path('', views.home, name='home'),

]
