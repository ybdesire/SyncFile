import json
import uuid
import datetime
import pytz#http://stackoverflow.com/questions/2331592/datetime-datetime-utcnow-why-no-tzinfo
from .models import UserAuthID

def create_json_response(auth_time, error_code, msg, status):
	json_response = json.loads('{}')
	json_response['auth_time'] = auth_time
	json_response['error_code'] = error_code
	json_response['msg'] = msg
	json_response['status'] = status
	return json_response

def is_valid_authid(req_auth_id):
	if( UserAuthID.objects.filter(authID = req_auth_id) ):
		past_time = UserAuthID.objects.filter(authID = req_auth_id)[0].authTime
		current_time = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
		delta_seconds = (current_time-past_time).total_seconds()
		if( delta_seconds>0 and delta_seconds<20*60*60):#authID not exceed 20h
			return True
	return False
	
def api_isAuthAlive(request):
	req_auth_id = request.GET.get('authid', '')
	if(is_valid_authid(req_auth_id)):
		past_time = UserAuthID.objects.filter(authID = req_auth_id)[0].authTime
		response_data = create_json_response('UTC: {0}'.format(past_time.strftime("%Y-%m-%d %H:%M:%S")), 1020, 'valid authid, and auth still alive', 'success')
	else:
		response_data = create_json_response('', 1021, 'invalid authid', 'error')
	return response_data