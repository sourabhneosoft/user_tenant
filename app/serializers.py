"""
    Serializers for the apis
"""

from rest_framework import serializers
from app.models import Question, Answer


class AnsSerializer(serializers.ModelSerializer):
    """
        Serializer for answer model
    """
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Answer
        fields = ('body', 'user')


class QuesSerializer(serializers.ModelSerializer):
    """
        Serializer class for Quetion model
    """
    answers = AnsSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'answers')
