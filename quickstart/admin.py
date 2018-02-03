# -*- coding: utf-8 -*-

from django.contrib import admin
from quickstart.models import Comment, Event

# Register your models here.

admin.site.register(Comment)
admin.site.register(Event)