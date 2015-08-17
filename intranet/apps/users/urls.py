# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^(?:/(?P<user_id>\d+))?$", views.profile_view, name="user_profile"),
    url(r"^/picture/(?P<user_id>\d+)(?:/(?P<year>freshman|sophomore|junior|senior))?$", views.picture_view, name="profile_picture"),

    url(ur"^/class/(?P<section_id>.*)?$", views.class_section_view, name="class_section"),
]
