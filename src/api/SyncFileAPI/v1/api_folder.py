import json
import os
import uuid
import datetime
import pytz#http://stackoverflow.com/questions/2331592/datetime-datetime-utcnow-why-no-tzinfo
from . import file_manage
from .models import UserAuthID, FileSys

def create_basic_json_response(error_code, msg, status):
	json_response = json.loads('{}')
	json_response['error_code'] = error_code
	json_response['msg'] = msg
	json_response['status'] = status
	return json_response

def create_json_response_for_folder_api_getdetail(error_code, msg, status, folder_details):
	json_response = json.loads('{}')
	json_response['error_code'] = error_code
	json_response['msg'] = msg
	json_response['status'] = status
	json_response['details'] = folder_details
	return json_response

	
def mkdir(req_path, req_username):
	'''req_path should be formated like 'asdf\\xxx', not 'asdf\\xxx\\'
	'''
	folder_path = os.path.join(req_username, req_path)
	mgr = file_manage.fileManage()
	
	if(mgr.is_exists(folder_path)):
		response_data = create_basic_json_response(1101, 'folder already exist', 'error')
	else:
		stat = mgr.create_folder(folder_path)
		if(stat[0]):
			response_data = create_basic_json_response(1100, 'folder created successfully', 'success')
			parent_folder_path = os.path.dirname(folder_path)
			parent_folder_id = FileSys.objects.filter(path=parent_folder_path)[0].id 
			
			folder_guid = str(uuid.uuid1()).replace('-', 'x')
			folder_parentid = parent_folder_id
			folder_type = 'folder'
			folder_size = '0'
			folder_current_date = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
			folder_creator = req_username
			folder_foldername = os.path.basename(req_path)
	
			folder_item = FileSys(id=folder_guid, parentid=folder_parentid, type=folder_type, size=folder_size, createdate=folder_current_date, creator=folder_creator, foldername=folder_foldername, path=folder_path)
			folder_item.save()
		else:
			response_data = create_basic_json_response(1102, 'folder path error. the parent folde should be created firstly. and use \\', 'error')
	return response_data

def get_folder_detail(req_path, req_username):
	if(req_path != 'root'):
		folder_path = os.path.join(req_username, req_path)
		parent_folder_path = os.path.dirname(folder_path)
	else:
		folder_path = '{0}'.format(req_username, req_path)
		parent_folder_path = folder_path
		
	if(FileSys.objects.filter(path=folder_path) and FileSys.objects.filter(path=parent_folder_path)):
		folder_details = json.loads('{}')
		folder_details['id'] = FileSys.objects.filter(path=folder_path)[0].id
		folder_details['parentid'] = FileSys.objects.filter(path=folder_path)[0].parentid
		folder_details['type'] = FileSys.objects.filter(path=folder_path)[0].type
		folder_details['size'] = FileSys.objects.filter(path=folder_path)[0].size
		folder_details['createdate'] = FileSys.objects.filter(path=folder_path)[0].createdate.strftime("%Y-%m-%d %H:%M:%S") + ' UTC'
		folder_details['creator'] = FileSys.objects.filter(path=folder_path)[0].creator
		folder_details['filename'] = FileSys.objects.filter(path=folder_path)[0].filename
		folder_details['foldername'] = FileSys.objects.filter(path=folder_path)[0].foldername
		folder_details['path'] = FileSys.objects.filter(path=folder_path)[0].path
		
		response_data = create_json_response_for_folder_api_getdetail(1120, 'folder details info', 'success', folder_details)
	else:
		response_data = create_json_response_for_folder_api_getdetail(1121, 'foler not exist. please check path format & content', 'error', '')
		
	return response_data
	
def rename_folder(req_username, src_path, dst_name):
	folder_path_db = os.path.join(req_username, src_path)
	folder_path = os.path.join(req_username, src_path)
	if(FileSys.objects.filter(path=folder_path_db)):
		if(os.path.dirname(src_path)!=''):
			dst_path = os.path.join(req_username, os.path.dirname(src_path), dst_name)
		else:
			dst_path = os.path.join(req_username, dst_name)
		for file_obj in FileSys.objects.all():
			if(file_obj.path.find(folder_path_db)==0):
				file_obj.path = file_obj.path.replace(folder_path_db, dst_path)
				file_obj.save()
		mgr = file_manage.fileManage()
		mgr.rename_folder(folder_path, dst_name)
		response_data = create_basic_json_response(1130, 'renamed folder {0} to {1}'.format(os.path.basename(src_path), dst_name), 'success')
	else:
		response_data = create_basic_json_response(1131, 'requested folder not exist', 'error')
	return response_data

def remove_folder(req_username, req_path):
	folder_path_db = os.path.join(req_username, req_path)
	folder_path = os.path.join(req_username, req_path)
	if(FileSys.objects.filter(path=folder_path_db)):
		for file_obj in FileSys.objects.all():
			if(file_obj.path.find(folder_path_db)==0):
				file_obj.delete()
		mgr = file_manage.fileManage()
		status = mgr.delete_folder(folder_path)
		response_data = create_basic_json_response(1140, 'folder removed', 'success')
	else:
		response_data = create_basic_json_response(1141, 'requested folder not exist. or path format error(use /)', 'error')
	return response_data

def list_folder(req_username, req_path):
	if(req_path=='root'):
		folder_path_db = '{0}'.format(req_username)
	else:
		folder_path_db = os.path.join(req_username, req_path)
		
	if(FileSys.objects.filter(path=folder_path_db)):
		folder_list = []
		for file_obj in FileSys.objects.all():
			if(file_obj.path.find(folder_path_db)==0 and file_obj.path!=folder_path_db):
				folder_list.append( '\\'.join(os.path.split(file_obj.path)[1:]))
		response_data = create_json_response_for_folder_api_getdetail(1150, 'get folder list', 'success', folder_list)
	else:
		response_data = create_basic_json_response(1151, 'requested folder not exist. or path format error(use /)', 'error')
	return response_data
	
def api_folder(request):
	'''authid should be validated before this function'''
	req_op = request.GET.get('op', '')
	req_path = request.GET.get('path', '').strip()
	req_auth_id = request.GET.get('authid', '')
	req_folder_dst_name = request.GET.get('name', '')
	req_username = UserAuthID.objects.filter(authID = req_auth_id)[0].userName
	response_data = ''
	
	#path format validation
	if(req_path.split('\\')[len(req_path.split('\\'))-1] == ''):
		response_data = create_basic_json_response(1103, 'folder path should not ended with \\', 'error')
		return response_data
	
	if(req_op=='mkdir'):
		response_data = mkdir(req_path, req_username)
	elif(req_op=='getdetail'):
		response_data = get_folder_detail(req_path, req_username)
	elif(req_op=='rename'):
		response_data = rename_folder(req_username, req_path, req_folder_dst_name)
	elif(req_op=='rm'):
		response_data = remove_folder(req_username, req_path)
	elif(req_op=='list'):
		response_data = list_folder(req_username, req_path)
	
	return response_data