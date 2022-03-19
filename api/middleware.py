import json
from django.utils import timezone

from .models import User


class UpdateUserActivityMiddleware:
    """
        Custom middleware for updating user
        last login and last activities timestamps
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/api/token/' and request.method == 'POST':
            data = json.loads(request.body)

        response = self.get_response(request)

        # update user last login and ip
        if request.path == '/api/token/' and response.status_code == 200:
            User.objects.filter(username=data['username']).update(
                last_login=timezone.now(),
                login_IP=self.visitor_ip_address(request)
            )
        # update user last activity
        if request.user.is_authenticated:
            User.objects.filter(pk=request.user.id).update(
                last_activity=timezone.now(),
            )
        return response

    def visitor_ip_address(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
