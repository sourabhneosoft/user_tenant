# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from app.models import Question, Tenant


class TestQuestion(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Create owner for the location
        self.user = User.objects.create_user(username="username.soni",
                                             password="password1")
        self.user.set_password("password1")
        self.user.save()

        self.tenant = Tenant.objects.create(name="neosoft",
                                            api_key="23cb00a63d7945eba0ff5b846de1b728")
        token = Token.objects.create(user=self.user)
        self.access_token = 'Token ' + token.key

        Question.objects.create(title="What is Python", user=self.user)
        Question.objects.create(title="Private Question", user=self.user,
                                private=True)

    def test_get_questions_without_login(self):
        response = self.client.get('/apis/questions/')
        self.assertEqual(response.status_code, 401)

    def test_get_questions_without_tenant_key(self):
        response = self.client.get('/apis/questions/',
                                   HTTP_AUTHORIZATION=self.access_token)
        self.assertEqual(response.status_code, 403)

    def test_get_questions_with_login_tenant_key(self):
        response = self.client.get('/apis/questions/',
                                   HTTP_API_KEY=self.tenant.api_key,
                                   HTTP_AUTHORIZATION=self.access_token)
        self.assertEqual(response.status_code, 200)

    def test_private_question(self):
        response = self.client.get('/apis/questions/',
                                   HTTP_API_KEY=self.tenant.api_key,
                                   HTTP_AUTHORIZATION=self.access_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_get_questions_with_query_string(self):
        response = self.client.get('/apis/questions/?q=xyz',
                                   HTTP_API_KEY=self.tenant.api_key,
                                   HTTP_AUTHORIZATION=self.access_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        response = self.client.get('/apis/questions/?q=what',
                                   HTTP_API_KEY=self.tenant.api_key,
                                   HTTP_AUTHORIZATION=self.access_token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def teardown(self):
        User.objects.all().delete()
        Question.objects.all().delete()
