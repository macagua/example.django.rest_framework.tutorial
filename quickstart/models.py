# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Event's room numbers
ROOM1 = 101
ROOM2 = 102
ROOM3 = 102
ROOM4 = 201
ROOM_NUMBER = (
    (ROOM1, "101"),
    (ROOM2, "102"),
    (ROOM3, "103"),
    (ROOM4, "201"),
)


class BlogPost(models.Model):
    title = models.CharField(max_length=1000, help_text="Enter the post's title.")
    content = models.CharField(max_length=100, help_text="Enter the post's content.")
    created = models.DateTimeField(help_text="Enter the post's date that which was created.")

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                              related_name='post',
                              verbose_name='Blog Post')
    email = models.EmailField(help_text="Enter the comment's author email.")
    content = models.CharField(max_length=128, help_text="Enter the comment.")
    created = models.DateTimeField(help_text="Enter the comment's date that which was created.")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.content

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


class Event(models.Model):
    name = models.CharField(max_length=100,
        help_text="Enter the event's name.")
    description = models.CharField(max_length=100,
        help_text="Enter the event's description.")
    room_number = models.IntegerField(choices=ROOM_NUMBER, default=ROOM4,
        help_text="Select the event's room number.")
    start_date = models.DateTimeField(help_text="Select the event's start date.")
    finish_date = models.DateTimeField(help_text="Select the event's finish date.")

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name
