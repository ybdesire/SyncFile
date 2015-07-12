from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from . import api_user_register
# Create your views here.

def index(request):
	return HttpResponse('index')
	

def userRegister(request):
	response_data = api_user_register.API_UserRegister(request)
	return HttpResponse(json.dumps(response_data), content_type='application/json')