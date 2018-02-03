# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from quickstart.models import Comment, Event
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')


class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


class ContactForm(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()

    def save(self):
        email = self.validated_data['email']
        message = self.validated_data['message']
        subject = '[Website] A Test'
        to_send = 'hello@mail.com'
        send_mail(subject, message, email, [to_send])


class EventSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(max_length=100)
    room_number = serializers.IntegerField()
    start_date = serializers.DateTimeField()
    finish_date = serializers.DateTimeField()

    class Meta:
        # Each room only has one event per day.
        validators = UniqueTogetherValidator(
            queryset=Event.objects.all(),
            fields=['room_number', 'start_date', 'finish_date']
        )

    def validate(self, data):
        """
        Check that the start date is before the stop.
        """
        if data['start_date'] > data['finish_date']:
            raise serializers.ValidationError("finish date must occur after start date")
        return data


class GameRecord(serializers.Serializer):
    score = serializers.IntegerField(validators=[multiple_of_ten])


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
