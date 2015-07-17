import json
import uuid
import datetime
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from .models import UserInfo
from .models import UserAuthID

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
	if ( UserInfo.objects.filter(userName = req_user_name) and check_password(req_password, password_at_db) ):
		if( not UserAuthID.objects.filter(userName = req_user_name) ):#user not exist at UserAuthID table. Create an item(userName, authID, authTime)
			guid = str(uuid.uuid1())
			ua = UserAuthID(userName=req_user_name, authID=guid, authTime=datetime.datetime.now())
			response_data = createJsonResponseForGetAuthID(guid, '1010', 'auth success')
		elif(UserAuthID.objects.filter(userName = req_user_name)[0].authID):#if authID exceed 20h, update authTime & authID. else return the exists authID
		else:#Create authTime & authID
			
		
		
	else:
		response_data = createJsonResponseForGetAuthID('', '1011', 'auth failure. user is not registed or user name/password incorrect')
	return response_data