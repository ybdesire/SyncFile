from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^userRegister$', views.userRegister, name='userRegister'),
	url(r'^getAuthID$', views.getAuthID, name='getAuthID'),
	url(r'^isAuthAlive$', views.isAuthAlive, name='isAuthAlive'),
]