# -*- coding: utf-8 -*-

from django.contrib import admin
from quickstart.models import BlogPost, Comment, Event


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created', 'email', 'blog_post')
    list_filter = ['email', 'created']
    search_fields = ['content']

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'finish_date')
    list_filter = ['start_date', 'finish_date']
    search_fields = ['name', 'description']

admin.site.register(BlogPost)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Event, EventAdmin)
