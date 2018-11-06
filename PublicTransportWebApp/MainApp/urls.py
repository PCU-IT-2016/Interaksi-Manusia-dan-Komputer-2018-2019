from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^$", views.home, name="index"),
    url(r"^contact/", views.contact, name="contact"),
    url(r"^schedule_list/(?P<pk>\d+)$", views.schedule_list, name='list'),
    url(r"^schedule_detail/(?P<pk>\d+)$", views.schedule_detail, name='detail'),
    url(r"^login/", views.login, name='login'),
    url(r"^new_home/", views.new_home, name="new_home"),
    url(r"^map/", views.map, name="new_home"),
    url(r"^register/", views.register_form, name="register_form"),
]