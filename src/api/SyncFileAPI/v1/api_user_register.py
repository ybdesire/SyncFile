from django.shortcuts import render
from django.http import HttpResponse
import json
import uuid
import datetime
import pytz#http://stackoverflow.com/questions/2331592/datetime-datetime-utcnow-why-no-tzinfo
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from .models import UserInfo, FileSys
from . import file_manage

def isStrEmpty(str):
	if str and str.strip():# if string empty or blank
		return False
	else:
		return True

def createJsonResponseForUserRegister(register_status, error_code, msg):#error code = 100x
	json_response = {}
	json_response['register_status']=register_status		
	json_response['error_code']=error_code
	json_response['msg']=msg
	return json_response

def createRootFolderForNewUser(user_name):
	mgr = file_manage.fileManage()
	mgr.create_folder(user_name)
	
	folder_guid = str(uuid.uuid1()).replace('-', 'x')
	folder_parentid = 'root'
	folder_type = 'folder'
	folder_size = '0'
	folder_current_date = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
	folder_creator = user_name
	folder_foldername = user_name
	folder_path = user_name+'\\'
	
	folder_item = FileSys(id=folder_guid, parentid=folder_parentid, type=folder_type, size=folder_size, createdate=folder_current_date, creator=folder_creator, foldername=folder_foldername, path=folder_path)
	folder_item.save()
	
def API_UserRegister(request):
	req_user_name = request.GET.get('username', '')
	req_password = request.GET.get('password', '')
	req_email = request.GET.get('email', '')
	
	response_data = {}
	
	special_characters = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
	for spch in special_characters:
		if spch in req_user_name:
			response_data = createJsonResponseForUserRegister('error', 1004, 'username cannot contain the following characters: \/:*?"<>|')
			return response_data
	
	if not (isStrEmpty(req_user_name) or isStrEmpty(req_password) or isStrEmpty(req_email)):
		if not ( UserInfo.objects.filter(userName = req_user_name) or UserInfo.objects.filter(email=req_email)):		
			response_data = createJsonResponseForUserRegister('ok', 1000, 'registered a new user.')
			q = UserInfo(userName=req_user_name, password=make_password(req_password), email=req_email)
			q.save()
			createRootFolderForNewUser(req_user_name)
		elif UserInfo.objects.filter(userName = req_user_name):
			response_data = createJsonResponseForUserRegister('error', 1001, 'the user has been registered, please change the user name.')
		elif UserInfo.objects.filter(email=req_email):
			response_data = createJsonResponseForUserRegister('error', 1002, 'the email has been registered, please change the email.')
	else:
		response_data = createJsonResponseForUserRegister('error', 1003, 'blank username/password/email')
	
	return response_data
