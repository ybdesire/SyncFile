import json
import uuid
import datetime
import pytz#http://stackoverflow.com/questions/2331592/datetime-datetime-utcnow-why-no-tzinfo
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
	if(UserInfo.objects.filter(userName = req_user_name)):
		password_at_db = UserInfo.objects.filter(userName = req_user_name)[0].password#the password at db is encrypted
		if ( UserInfo.objects.filter(userName = req_user_name) and check_password(req_password, password_at_db) ):
			if( not UserAuthID.objects.filter(userName = req_user_name) ):#user not exist at UserAuthID table. Create an item(userName, authID, authTime)
				guid = str(uuid.uuid1())
				ua = UserAuthID(userName=req_user_name, authID=guid, authTime=datetime.datetime.utcnow())
				ua.save()
				response_data = createJsonResponseForGetAuthID(guid, '1010', 'auth success')
			elif(UserAuthID.objects.filter(userName = req_user_name)[0].authID):#if authID exceed 20h, update authTime & authID. else return the exists authID
				past_time = UserAuthID.objects.filter(userName = req_user_name)[0].authTime
				current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
				delta_seconds = (current_time-past_time).total_seconds()
				if( delta_seconds>0 and delta_seconds<20*60*60):#authID not exceed 20h, return the exist authID
					guid = UserAuthID.objects.filter(userName = req_user_name)[0].authID
					response_data = createJsonResponseForGetAuthID(guid, '1010', 'auth success')
				else:
					guid = str(uuid.uuid1())
					current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
					ua = UserAuthID.objects.filter(userName = req_user_name)[0]
					ua.authID = guid
					ua.authTime = current_time
					ua.save()
					response_data = createJsonResponseForGetAuthID(guid, '1010', 'auth success')
			else:#Create authTime & authID
				guid = str(uuid.uuid1())
				current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
				ua = UserAuthID.objects.filter(userName = req_user_name)[0]
				ua.authID = guid
				ua.authTime = current_time
				response_data = createJsonResponseForGetAuthID(guid, '1010', 'auth success')
		else:
			response_data = createJsonResponseForGetAuthID('', '1011', 'auth failure. user is not registed or user name/password incorrect')
	else:
		response_data = createJsonResponseForGetAuthID('', '1011', 'auth failure. user is not registed or user name/password incorrect')
	return response_data