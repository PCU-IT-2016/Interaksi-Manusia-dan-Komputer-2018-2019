from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.home, name="index"),
    url(r"^contact/", views.contact, name="contact"),
    url(r"^home/(?P<pk>\d+)$", views.info, name='info'),
    url(r"^login/", views.login, name='login'),
]