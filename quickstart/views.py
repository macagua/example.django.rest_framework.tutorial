# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.models import BlogPost, Comment, Event
from quickstart.serializers import CommentSerializer, BlogPostSerializer, EventSerializer, UserSerializer, GroupSerializer



class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Blog posts to be viewed or edited.
    """
    queryset = BlogPost.objects.all().order_by('-created')
    serializer_class = BlogPostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('-start_date')
    serializer_class = EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
