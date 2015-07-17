import json
import uuid
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from .models import UserInfo

def createJsonResponseForGetAuthID(authid, error_code, msg):
	json_response = {}
	json_response['authid'] = authid
	json_response['error_code'] = error_code
	json_response['msg'] = msg
	return json_response

def API_GetAuthID(request):
	req_user_name = request.GET.get('username', '')
	req_password = request.GET.get('password', '')
	
	response_data = {}
	
	password_at_db = UserInfo.objects.filter(userName = req_user_name)[0].password#the password at db is encrypted
	if ( UserInfo.objects.filter(userName = req_user_name) and check_password(req_password, password_at_db)):
		response_data = createJsonResponseForGetAuthID(str(uuid.uuid1()), '1010', 'auth success')
	else:
		response_data = createJsonResponseForGetAuthID('', '1011', 'auth failure. user is not registed or user name/password incorrect')
	return response_data