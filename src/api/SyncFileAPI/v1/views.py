from django.shortcuts import render
from django.http import HttpResponse
from .models import UserAuthID
import json
import datetime
import pytz
import urllib
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from . import api_user_register
from . import api_get_authid
from . import api_is_auth_alive
from . import api_folder, api_file
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
	return HttpResponse('index')
	
def userRegister(request):
	response_data = api_user_register.api_userRegister(request)
	return HttpResponse(json.dumps(response_data), content_type='application/json')

def getAuthID(request):
	response_data = api_get_authid.api_getAuthID(request)
	return HttpResponse(json.dumps(response_data), content_type='application/json')
	
def isAuthAlive(request):
	response_data = api_is_auth_alive.api_isAuthAlive(request)
	return HttpResponse(json.dumps(response_data), content_type='application/json')
	
def folder(request):
	req_auth_id = request.GET.get('authid', '')
	if( api_is_auth_alive.is_valid_authid(req_auth_id) ):
		response_data = api_folder.api_folder(request)
	else:
		response_data = api_is_auth_alive.create_json_response('', 1021, 'invalid authid', 'error')
	return HttpResponse(json.dumps(response_data), content_type='application/json')

@csrf_exempt# tell the view not check csrf token for POST file request
def file(request):
	req_auth_id = request.GET.get('authid', '')
	if( api_is_auth_alive.is_valid_authid(req_auth_id) ):
		response_data = api_file.api_file(request)
	else:
		response_data = api_is_auth_alive.create_json_response('', 1021, 'invalid authid', 'error')
	return HttpResponse(json.dumps(response_data), content_type='application/json')

#process short link. such as 'http://localhost:8000/v1/f/?id=09fe2870-5cdf-11e5-8d49-ea9f05b65156'
def f(request):
	short_id = request.GET.get('id', '')
	file_name, file_data = api_file.get_download_file_data(short_id)
	response = HttpResponse(file_data, content_type='text/plain')
	#support Unicode file name. [IE9,Chrome,FF]
	response['Content-Disposition'] = 'attachment; filename="{0}";filename*=UTF-8\'\'{1}'.format(urllib.parse.quote_plus(file_name), urllib.parse.quote_plus(file_name))

	return response