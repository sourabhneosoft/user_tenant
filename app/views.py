# -*- coding: utf-8 -*-
"""
Views module
"""

from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

# Create your views here.
from app.models import Question, Answer, Tenant


class HomeDashboard(View):
    """
        Home dashboard View
    """

    def get(self, request):
        """

        :param request:
        :return: Will return dashboard page with count
        """
        total_users = User.objects.all().count()
        total_answers = Answer.objects.all().count()
        total_questions = Question.objects.all().count()
        tenants = Tenant.objects.all()
        return render(request, "home_dashboard.html",
                    {'total_users': total_users,
                      'total_answers': total_answers,
                      'total_questions': total_questions,
                      'tenants': tenants})
