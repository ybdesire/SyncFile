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
		
class UserToken(models.Model):
	userName = models.CharField(max_length=200)
	authID = models.CharField(max_length=200)
	authTime = models.TimeField(blank=True)