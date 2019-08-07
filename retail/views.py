from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect



def index(request):
    if request.user.is_authenticated:
        return HttpResponse("Hello, world. You're at the retail index.")
    else:
        return HttpResponseRedirect('/auth/login')
