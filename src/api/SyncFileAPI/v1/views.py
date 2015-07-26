from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAuthID
import json
import datetime
import pytz
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from . import api_user_register
from . import api_get_authid
from . import api_is_auth_alive
from . import api_folder
# Create your views here.


def index(request):
	return HttpResponse('index')
	
def userRegister(request):
	response_data = api_user_register.API_UserRegister(request)
	return HttpResponse(json.dumps(response_data), content_type='application/json')

def getAuthID(request):
	response_data = api_get_authid.API_GetAuthID(request)
	return HttpResponse(json.dumps(response_data), content_type='application/json')
	
def isAuthAlive(request):
	response_data = api_is_auth_alive.API_isAuthAlive(request)
	return HttpResponse(json.dumps(response_data), content_type='application/json')
	
def folder(request):
	req_auth_id = request.GET.get('authid', '')
	if( api_is_auth_alive.isValidAuthID(req_auth_id) ):
		response_data = api_folder.API_folder(request)
	else:
		response_data = api_is_auth_alive.createJsonResponseForisAuthAlive('', 1021, 'invalid authid')
	return HttpResponse(json.dumps(response_data), content_type='application/json')
