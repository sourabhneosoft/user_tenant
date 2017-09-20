"""
    Viewset for Question
"""

from app.models import Question
from app.serializers import QuesSerializer
from app.perms import IsProvidedApiKey
from app.throttle import TenantThrottle
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class QuesViewSet(viewsets.ReadOnlyModelViewSet):
    """
        Viewset for Question
    """
    permission_classes = (IsAuthenticated, IsProvidedApiKey)
    queryset = Question.objects.all()
    serializer_class = QuesSerializer
    throttle_classes = (TenantThrottle,)

    def get_queryset(self):
        query_params = self.request.GET.get('q')
        if query_params:
            queryset = self.request.user.question_set.filter(private=False,
                                                          title__contains=query_params)
        else:
            queryset = self.request.user.question_set.filter(private=False)

        return queryset
