from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.hashers import make_password, check_password, is_password_usable

from .models import UserInfo
# Create your views here.

def index(request):
	return HttpResponse('index')
	

def isStrEmpty(str):
	if str and str.strip():
		return False
	else:
		return True

def createJsonResponseForUserRegister(register_status, error_code, msg):
	json_response = {}
	json_response["register_status"]=register_status		
	json_response["error_code"]=error_code
	json_response["msg"]=msg
	return json_response

def userRegister(request):
	req_user_name = request.GET.get('username', '')
	req_password = request.GET.get('password', '')
	req_email = request.GET.get('email', '')
	
	response_data = {}
	
	if not (isStrEmpty(req_user_name) or isStrEmpty(req_password) or isStrEmpty(req_email)):
		if not ( UserInfo.objects.filter(userName = req_user_name) or UserInfo.objects.filter(email=req_email)):
			response_data = createJsonResponseForUserRegister('ok', 1000, 'registered a new user.')
			print('passwd: {0}'.format(make_password(req_password)))
			q = UserInfo(userName=req_user_name, password=make_password(req_password), email=req_email)
			q.save()
		elif UserInfo.objects.filter(userName = req_user_name):
			response_data = createJsonResponseForUserRegister('error', 1001, 'the user has been registered, please change the user name.')
		elif UserInfo.objects.filter(email=req_email):
			response_data = createJsonResponseForUserRegister('error', 1002, 'the email has been registered, please change the email.')
	else:
		response_data = createJsonResponseForUserRegister('error', 1003, 'blank username/password/email')
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")
	