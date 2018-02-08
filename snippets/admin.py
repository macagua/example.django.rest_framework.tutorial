# -*- coding: utf-8 -*-

from django.contrib import admin

from snippets.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'linenos', 'language', 'style')
    list_filter = ['code', 'language']
    search_fields = ['title', 'code'] # created

admin.site.register(Snippet, SnippetAdmin)
