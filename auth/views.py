from django.forms import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate as authenticate_user
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
import util.constancts as constancts
import util.common as common
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    return JsonResponse(common.COMMON_SUCCESS_RESPONSE)


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate_user(request, username=username, password=password)
    if user is not None:
        login_user(request, user)
        res = common.COMMON_SUCCESS_RESPONSE
        res['user'] = model_to_dict(user)
        return JsonResponse(res)
    else:
        # Return an 'invalid login' error message.
        return JsonResponse({'status': constancts.RET_FAILURE, 'msg': 'User not registered or password incorrect.'})


def logout(request):
    logout_user(request)
    return JsonResponse(common.COMMON_SUCCESS_RESPONSE)
