"""
Throttle module
"""

import datetime

from rest_framework.throttling import BaseThrottle

from app.models import Tenant, ThrottleRequest


class TenantThrottle(BaseThrottle):
    """
        TenantThrottle class
    """

    def allow_request(self, request, view):
        """
        allow request checking.
        """
        now = datetime.datetime.now()
        api_key = request.META.get('HTTP_API_KEY')
        tenant = Tenant.objects.get(api_key=api_key)
        todays_requests = ThrottleRequest.objects.filter(tenant=tenant,
                            requested_on__date=datetime.datetime.today())
        is_allowed = True

        if len(todays_requests) > 50 and todays_requests.filter(
            requested_on__gte=datetime.datetime.now() -
            datetime.timedelta(seconds=10)):
            is_allowed = False

        if is_allowed:
            ThrottleRequest.objects.create(tenant=tenant, requested_on=now,
                                   requested_by=request.user, url=request.path)
        return is_allowed
