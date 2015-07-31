from django.test import TestCase
import unittest
import requests
import json

# Create your tests here.
class TestAPIv1(unittest.TestCase):
	def test_api_userRegister_1000(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=userxxx&password=password&email=userxxx@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1000)

	def test_api_userRegister_1001(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=testuser1&password=password&email=user@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1001)

	def test_api_userRegister_1002(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=userx&password=password&email=testuser1@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1002)

	def test_api_userRegister_1003(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username= &password=password&email=user@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1003)
		
	def test_api_getAuthID_1011(self):
		req = requests.get('http://localhost:8000/v1/getAuthID?username=xxxx&password=password')#unknown username or password
		answer = req.json()
		self.assertEqual(answer['error_code'], 1011)
	
	def test_api_getAuthID_1010(self):
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		self.assertEqual(answer['error_code'], 1010)
	
	def test_api_isAuthAlive_1021(self):
		req = requests.get('http://localhost:8000/v1/isAuthAlive?authid=xxxxx')#non-exist authid
		answer = req.json()
		self.assertEqual(answer['error_code'], 1021)

	def test_api_isAuthAlive_1020(self):
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/isAuthAlive?authid={0}'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1020)
	
	def test_api_folder_mkdir_1100(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1100)
		
	def test_api_folder_mkdir_1101(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1101)
		
	def test_api_folder_mkdir_1102(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book\lol\ooo\lol\ooo'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1102)
		
	def test_api_folder_mkdir_1103(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book\lol\\'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1103)
		
	def test_api_folder_detail_1120_root(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=getdetail&authid={0}&path=root'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1120)

	def test_api_folder_detail_1120_path(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=testdir'.format(answer['authid']))
		req = requests.get('http://localhost:8000/v1/folder?op=getdetail&authid={0}&path=testdir'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1120)

		
	def test_api_folder_detail_1121(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=getdetail&authid={0}&path=xxx\ooo'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1121)