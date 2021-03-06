"""
    Permission for restframework
"""

from rest_framework.permissions import BasePermission

from app.models import Tenant


class IsProvidedApiKey(BasePermission):
    """
    Permission class for checking api key.
    """
    def has_permission(self, request, view):

        api_key = request.META.get('HTTP_API_KEY')
        if not api_key:
            return False
        else:
            try:
                Tenant.objects.get(api_key=api_key)
                return True
            except Tenant.DoesNotExist:
                return False
