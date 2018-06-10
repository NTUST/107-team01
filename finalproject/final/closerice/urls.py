from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
    url(r'^taipei_1/$',views.taipei_1),
    url(r'^haha/$',views.haha),
    url(r'^hahaeditpage/$',views.hahaeditpage),
]