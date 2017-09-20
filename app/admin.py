# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import Question, Answer, Tenant
# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
        ModelAdmin for Question model
    """
    list_display = ('id', 'title', 'private', 'user',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """
        ModelAdmin for AnswerAdmin model
    """
    list_display = ('id', 'body', 'question', 'user',)


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    """
        ModelAdmin for TenantAdmin
    """
    list_display = ('id', 'name', 'api_key',)