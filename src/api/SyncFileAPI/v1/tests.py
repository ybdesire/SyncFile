from django.test import TestCase
import unittest
import requests
import json

# Create your tests here.
class TestAPIv1(unittest.TestCase):
	def test_API_UserRegister_1000(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=userxxx&password=password&email=userxxx@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1000)

	def test_API_UserRegister_1001(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=user&password=password&email=user@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1001)

	def test_API_UserRegister_1002(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=userx&password=password&email=user@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1002)

	def test_API_UserRegister_1003(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username= &password=password&email=user@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1003)
		
	def test_API_getAuthID_1011(self):
		req = requests.get('http://localhost:8000/v1/getAuthID?username=xxxx&password=password')#unknown username or password
		answer = req.json()
		self.assertEqual(answer['error_code'], 1011)
	
	def test_API_getAuthID_1010(self):
		req = requests.get('http://localhost:8000/v1/getAuthID?username=user1&password=123')#exist username & password
		answer = req.json()
		self.assertEqual(answer['error_code'], 1010)
	
