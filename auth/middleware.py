from django.http import HttpResponseForbidden
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
import re

# 不需要拦截的请求
ALLOW_REQUEST_PATH = [
    r'^/auth/*',
    r'.*favicon.ico.*',
]


# 用于统一拦截请求
class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        for url in ALLOW_REQUEST_PATH:
            if request.path == "/" or re.match(url, request.path):
                # 如果匹配到允许的url则直接通行
                return
        else:
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Please make sure you are logged in.")
            else:
                request.session['last_access_time'] = timezone.now()
                request.session.modified = True
                response = self.get_response(request)
                return response
