from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('category/', category, name="category"),
]
