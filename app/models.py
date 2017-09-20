
"""
Models for User Tenant
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    """
        Model for Question
    """
    title = models.CharField(max_length=200)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    """
        Model for Answer
    """
    body = models.TextField()
    question = models.ForeignKey(Question, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class Tenant(models.Model):
    """
        Model for Tenant
    """
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class ThrottleRequest(models.Model):
    """
        Model for Throttle request
    """

    tenant = models.ForeignKey(Tenant, related_name='requests')

    url = models.CharField(max_length=100, null=False, blank=False)

    requested_on = models.DateTimeField(default=timezone.now)

    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='requests')

    