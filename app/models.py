# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Question(models.Model):
    """
        Model for Question
    """
    title = models.CharField(max_length=200)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Answer(models.Model):
    """
        Model for Answer
    """
    body = models.TextField()
    question = models.ForeignKey(Question)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Tenant(models.Model):
    """
        Model for Tenant
    """
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=50)