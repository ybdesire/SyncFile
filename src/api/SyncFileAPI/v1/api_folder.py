import json
import os
import uuid
import datetime
import pytz#http://stackoverflow.com/questions/2331592/datetime-datetime-utcnow-why-no-tzinfo
from . import file_manage
from .models import UserAuthID, FileSys

def create_json_response_for_folder_api_mkdir(error_code, msg, status):
	json_response = {}
	json_response['error_code'] = error_code
	json_response['msg'] = msg
	json_response['status'] = status
	return json_response

def create_json_response_for_folder_api_getdetail(error_code, msg, status):
	json_response = {}
	json_response['error_code'] = error_code
	json_response['msg'] = msg
	json_response['status'] = status
	
	return json_response

	
def mkdir(req_path, req_username):
	'''req_path should be formated like 'asdf\\xxx', not 'asdf\\xxx\\'
	'''
	folder_path = '{0}\\{1}'.format(req_username, req_path)
	mgr = file_manage.fileManage()
	
	if(mgr.is_exists(folder_path)):
		response_data = create_json_response_for_folder_api_mkdir(1101, 'folder already exist', 'error')
	elif(folder_path.split('\\')[len(folder_path.split('\\'))-1] == ''):
		response_data = create_json_response_for_folder_api_mkdir(1103, 'folder path should not ended with \\', 'error')
	else:
		stat = mgr.create_folder(folder_path)
		if(stat[0]):
			response_data = create_json_response_for_folder_api_mkdir(1100, 'folder created successfully', 'success')
			parent_folder_path = os.path.dirname(folder_path) + '\\'	#DB path should be ended with '\\', such as 'asdf\\xxx\\'
			parent_folder_id = FileSys.objects.filter(path=parent_folder_path)[0].id 
			
			folder_guid = str(uuid.uuid1()).replace('-', 'x')
			folder_parentid = parent_folder_id
			folder_type = 'folder'
			folder_size = '0'
			folder_current_date = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
			folder_creator = req_username
			folder_foldername = os.path.basename(req_path)
	
			folder_item = FileSys(id=folder_guid, parentid=folder_parentid, type=folder_type, size=folder_size, createdate=folder_current_date, creator=folder_creator, foldername=folder_foldername, path=folder_path+'\\')
			folder_item.save()
		else:
			response_data = create_json_response_for_folder_api_mkdir(1102, 'folder path error. the parent folde should be created firstly. and use \\', 'error')
	return response_data

def get_folder_detail(req_path, req_username):
	if(req_path != 'root'):
		folder_path = '{0}\\{1}\\'.format(req_username, req_path)
		parent_folder_path = os.path.dirname('{0}\\{1}'.format(req_username, req_path))
	else:
		folder_path = '{0}\\'.format(req_username, req_path)
		parent_folder_path(folder_path)

	return FileSys.objects.filter(path=folder_path)[0].id
	
def api_folder(request):
	'''authid should be validated before this function'''
	req_op = request.GET.get('op', '')
	req_path = request.GET.get('path', '').strip()
	req_auth_id = request.GET.get('authid', '')
	req_username = UserAuthID.objects.filter(authID = req_auth_id)[0].userName
	response_data = ''
	if(req_op=='mkdir'):
		response_data = mkdir(req_path, req_username)
	if(req_op=='getdetail'):
		response_data = get_folder_detail(req_path, req_username)
	
	return response_data