from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
import requests
import re
from django.http import JsonResponse

def index(request):
    if request.user.is_authenticated:
        return HttpResponse("Hello, world. You're at the retail index.")
    else:
        return HttpResponseRedirect('/auth/login')

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def api_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error_msg': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error_msg': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    login(request, user)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

@csrf_exempt   
def is_logged_in(request):
    regex = re.compile('^HTTP_')
    hedars = dict((regex.sub('', header), value) for (header, value)
            in request.META.items() if header.startswith('HTTP_')
        )
    print(request.user)
    lst_val_json = {}
    lst_val_json['is_logged_in'] = request.user.is_authenticated
    return JsonResponse(lst_val_json)