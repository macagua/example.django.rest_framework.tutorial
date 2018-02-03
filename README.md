# django_rest_framework_tutorial

My practices about [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/) and [Django Rest Framework 3.6.4 tutorial Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/).

## Installation

This Django Web app need a lot of Python extras packages, please execute the following command:

```bash
$ pip install -r requirements.txt --timeout 120
```

### Build the Django Web app DB

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
### Create Django Admin User

This Django Web app need a to create a Django Admin User, for access and manager the Admin interface, please execute the following command:

**Tip:** for this local installation use the user as **admin** and password as **password123**.

```bash
$ python manage.py createsuperuser --email admin@mail.com --username admin
Password: 
Password (again): 
Superuser created successfully.
```

## Run the Django Web app

You need to run the Django server, please execute the following command:

```bash
$ python manage.py runserver
```

- Open your web browser with the following URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) and see the Django Web app.

- Open your web browser with the following URL: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) and see the Django Admin Interface, use the user **admin** and password **password123**.

**Tip:** PLEASE add two **groups**, two **users** and later add a user into a group.

### Testing the API

You have 2 API Rest for testing, now access to the APIs, both from the command-line, using tools like **curl**, please execute the following command:

#### Users endpoint

For testing the **users** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/users/4/",
        "username": "rocio",
        "email": "rociogonzalez@mail.com",
        "groups": [
            "http://127.0.0.1:8000/groups/3/"
        ]
    },
    {
        "url": "http://127.0.0.1:8000/users/3/",
        "username": "leonardo",
        "email": "leonardo@mail.com",
        "groups": [
            "http://127.0.0.1:8000/groups/2/"
        ]
    },
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin",
        "email": "admin@mail.com",
        "groups": []
    }
]
```

#### Groups endpoint

For testing the **groups** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/groups/
[
    {
        "url": "http://127.0.0.1:8000/groups/1/",
        "name": "Administrators"
    },
    {
        "url": "http://127.0.0.1:8000/groups/2/",
        "name": "Plone"
    },
    {
        "url": "http://127.0.0.1:8000/groups/3/",
        "name": "Botana"
    }
]
```

#### Events endpoint

For testing the **events** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/events/
[
    {
        "name": "New Plone release for 2018",
        "description": "Plone will be release a new version at PloneConf 2018",
        "room_number": 201,
        "start_date": "2018-02-13T19:42:31Z",
        "finish_date": "2018-02-14T19:42:37Z"
    },
    {
        "name": "New Django release",
        "description": "Django will be release a new version at DjangoConf 2018",
        "room_number": 101,
        "start_date": "2018-02-12T19:40:59Z",
        "finish_date": "2018-02-12T20:41:04Z"
    }
]
```

#### Blog post endpoint

For testing the **blog post** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/blog-post/
[
    {
        "title": "Django project will be release a new version soon",
        "content": "Django will be release a new version at DjangoConf 2018"
    },
    {
        "title": "Plone is Cool",
        "content": "Plone is still in fashion with the latest Web technologies"
    }
]
```

#### Comments endpoint

For testing the **comments** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/comments/
[
    {
        "email": "leonardo@mail.com",
        "content": "I want to dowload and test it",
        "created": "2018-02-03T19:46:43Z"
    },
    {
        "email": "leonardoc@plone.org",
        "content": "#FuckYou Djanguero",
        "created": "2018-02-03T19:22:02Z"
    },
    {
        "email": "djangueroguy@djangoproject.com",
        "content": "You are very pathetic you are still using Plone",
        "created": "2018-02-03T19:21:33Z"
    }
]
```

## Django Interactive Console
For make some practices the Django ORM, please execute the following command:

```bash
$ python manage.py shell
Python 2.7.13 (default, Nov 24 2017, 17:33:09) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

At Python Interactive Console, please execute the following command:

```python
>>> 
>>> # Serializers tutorial section
>>> 
>>> # Declaring Serializers section
>>>
>>> from datetime import datetime
>>> 
>>> class Comment(object):
...     def __init__(self, email, content, created=None):
...         self.email = email
...         self.content = content
...         self.created = created or datetime.now()
... 
>>> comment = Comment(email='leonardo@mail.com', content='THIS IS A TESTING COMMENT')
>>> comment
<Comment object at 0x7f110aa91510>
>>> from rest_framework import serializers
>>> class CommentSerializer(serializers.Serializer):
...     email = serializers.EmailField()
...     content = serializers.CharField(max_length=200)
...     created = serializers.DateTimeField()
...
>>> 
>>> # Serializing objects section
>>>  
>>> serializer = CommentSerializer(comment)
>>> serializer
CommentSerializer(<Comment object>):
    email = EmailField()
    content = CharField(max_length=200)
    created = DateTimeField()
>>> serializer.data
{'email': u'leonardo@mail.com', 'content': u'THIS IS A TESTING COMMENT', 'created': '2018-02-03T14:51:39.574410'}
>>> from rest_framework.renderers import JSONRenderer
>>> json = JSONRenderer().render(serializer.data)
>>> json
'{"email":"leonardo@mail.com","content":"THIS IS A TESTING COMMENT","created":"2018-02-03T14:51:39.574410"}'
>>> 
>>> # Deserializing objects section
>>> 
>>> from django.utils.six import BytesIO
>>> from rest_framework.parsers import JSONParser
>>> 
>>> stream = BytesIO(json)
>>> data = JSONParser().parse(stream)
>>> data
{u'content': u'THIS IS A TESTING COMMENT', u'email': u'leonardo@mail.com', u'created': u'2018-02-03T15:16:41.744807'}
>>>
>>> serializer = CommentSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
OrderedDict([(u'email', u'leonardo@mail.com'), (u'content', u'THIS IS A TESTING COMMENT'), (u'created', datetime.datetime(2018, 2, 3, 14, 51, 39, 574410, tzinfo=<django.utils.timezone.LocalTimezone object at 0x7f1109752c90>))])
>>> 
>>> # Saving instances section
>>> 
>>> class CommentSerializer(serializers.Serializer):
... 
...     email = serializers.EmailField()
...     content = serializers.CharField(max_length=200)
...     created = serializers.DateTimeField()
...     def create(self, validated_data):
...         return Comment(**validated_data)
...     def update(self, instance, validated_data):
...         instance.email = validated_data.get('email', instance.email)
...         instance.content = validated_data.get('content', instance.content)
...         instance.created = validated_data.get('created', instance.created)
...         return instance
... 
>>>
>>> serializer = CommentSerializer(data=data)
>>> serializer = CommentSerializer(comment, data=data)
>>> 
>>> # Validation section
>>> 
>>> serializer = CommentSerializer(data={'email': 'foobar', 'content': 'baz'})
>>> serializer.is_valid()
False
>>> serializer.errors
{'email': [u'Enter a valid email address.'], 'created': [u'This field is required.']}
>>> 
>>> serializer.is_valid(raise_exception=True)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/leonardo/virtualenv/django27/local/lib/python2.7/site-packages/rest_framework/serializers.py", line 245, in is_valid
    raise ValidationError(self.errors)
ValidationError: {'email': [u'Enter a valid email address.'], 'created': [u'This field is required.']}
>>> 
>>> # Field-level validation section
>>> 
>>> from rest_framework import serializers
>>> class BlogPostSerializer(serializers.Serializer):
...     title = serializers.CharField(max_length=100)
...     content = serializers.CharField()
...     def validate_title(self, value):
...         """
...         Check that the blog post is about Django.
...         """
...         if 'django' not in value.lower():
...             raise serializers.ValidationError("Blog post is not about Django")
...         return value
... 
>>> 
>>> # Object-level validation section
>>>
>>> class EventSerializer(serializers.Serializer):
...     description = serializers.CharField(max_length=100)
...     start = serializers.DateTimeField()
...     finish = serializers.DateTimeField()
...     def validate(self, data):
...         """
...         Check that the start is before the stop.
...         """
...         if data['start'] > data['finish']:
...             raise serializers.ValidationError("finish must occur after start")
...         return data
... 
>>> 
>>> # Validators section
>>>
>>> def multiple_of_ten(value):
...     if value % 10 != 0:
...         raise serializers.ValidationError('Not a multiple of ten')
... 
>>> class GameRecord(serializers.Serializer):
...     score = serializers.IntegerField(validators=[multiple_of_ten])
... 
>>>  
```

# Reference

- [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/).
- [Django Rest Framework 3.6.4 tutorial Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/).
