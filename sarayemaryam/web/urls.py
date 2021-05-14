from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^account/register$', view=views.register_user),
    url(r'^account/login$', view=views.login_user)
]