from django.db import models
import datetime

# Create your models here.
class UserInfo(models.Model):
	userName = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	
	def __str__(self):
		return self.userName
	
	def getEmail(self):
		return self.email
	def getPasswd(self):
		return self.password
		
class UserAuthID(models.Model):
	userName = models.CharField(max_length=200)
	authID = models.CharField(max_length=50)
	authTime = models.DateTimeField(blank=True)
	
class FileSys(models.Model):
	id = models.CharField(max_length=50, primary_key=True)
	parentid = models.CharField(max_length=50)
	type = models.CharField(max_length=20)
	size = models.CharField(max_length=20)
	createdate = models.DateTimeField(blank=True)
	creator = models.CharField(max_length=200)
	filename = models.CharField(max_length=200, blank=True)
	foldername = models.CharField(max_length=200, blank=True)
	path = models.CharField(max_length=2000, blank=True)

class ShortLink(models.Model):
	id = models.CharField(max_length=50, primary_key=True)
	link = models.CharField(max_length=2000)