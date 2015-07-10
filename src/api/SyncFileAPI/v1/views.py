from django.shortcuts import render
from django.http import HttpResponse
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
	
def userRegister(request):
	req_user_name = request.GET.get('username', '')
	req_password = request.GET.get('password', '')
	req_email = request.GET.get('email', '')
	
	if not (isStrEmpty(req_user_name) or isStrEmpty(req_password) or isStrEmpty(req_email)):
		#for u in UserInfo.objects.all():
		#	print(u.password)
		if not ( UserInfo.objects.filter(userName = req_user_name) or UserInfo.objects.filter(email=req_email)):
			print('user added')
			print('passwd: {0}'.format(make_password(req_password)))
			q = UserInfo(userName=req_user_name, password=make_password(req_password), email=req_email)
			q.save()
		else:
			print('user already registed')
		return HttpResponse('not blank: ' + req_user_name)
	else:
		return HttpResponse('blank: ' + UserInfo())