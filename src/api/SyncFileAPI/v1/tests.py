from django.test import TestCase
import unittest
import requests
import json

# Create your tests here.
# Run single test case: manage.py test v1.tests.TestAPIV1.test005_api_getAuthID_101120
class TestAPIV1(unittest.TestCase):
	def test001_api_userRegister_1000(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=testuser2&password=123&email=testuser2@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1000)

	def test002_api_userRegister_1001(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=testuser1&password=password&email=user@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1001)
		
	def test003_api_userRegister_1002(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username=userx&password=password&email=testuser1@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1002)

	def test004_api_userRegister_1003(self):
		req = requests.get('http://localhost:8000/v1/userRegister?op=register&fmt=json&username= &password=password&email=user@email.com')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1003)
		
	def test005_api_getAuthID_1011(self):
		req = requests.get('http://localhost:8000/v1/getAuthID?username=xxxx&password=password')#unknown username or password
		answer = req.json()
		self.assertEqual(answer['error_code'], 1011)
	
	def test006_api_getAuthID_1010(self):
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		self.assertEqual(answer['error_code'], 1010)
		
	def test007_api_isAuthAlive_1021(self):
		req = requests.get('http://localhost:8000/v1/isAuthAlive?authid=xxxxx')#non-exist authid
		answer = req.json()
		self.assertEqual(answer['error_code'], 1021)

	def test008_api_isAuthAlive_1020(self):
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/isAuthAlive?authid={0}'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1020)

	def test009_api_folder_mkdir_1100(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1100)
		
	def test010_api_folder_mkdir_1101(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1101)
		
	def test011_api_folder_mkdir_1102(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book\lol\ooo\lol\ooo'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1102)
		
	def test012_api_folder_mkdir_1103(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book\lol\\'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1103)
		
	def test013_api_folder_detail_1120_root(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=getdetail&authid={0}&path=root'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1120)

	def test014_api_folder_detail_1120_path(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=testdir'.format(answer['authid']))
		req = requests.get('http://localhost:8000/v1/folder?op=getdetail&authid={0}&path=testdir'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1120)
	
	def test015_api_folder_detail_1121(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=getdetail&authid={0}&path=xxx\ooo'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1121)

	def test016_api_folder_rename_1130(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=rename&authid={0}&path=testdir&name=modified'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1130)
	
	def test017_api_folder_rename_1131(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=rename&authid={0}&path=notexistpath&name=modified'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1131)
		
	def test018_api_folder_rm_1140(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=rm&authid={0}&path=book'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1140)
		
	def test019_api_folder_rm_1141(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=rm&authid={0}&path=notexistpath'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1141)

	def test020_api_folder_list_root_1150(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=list&authid={0}&path=root'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1150)
		
	def test021_api_folder_list_path_1150(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=mkdir&authid={0}&path=book'.format(answer['authid']))
		req = requests.get('http://localhost:8000/v1/folder?op=list&authid={0}&path=book'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1150)
		
	def test022_api_folder_rm_1151(self):
		#make sure user testuser1 registered(in DB). And dir testuser1 existed
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		req = requests.get('http://localhost:8000/v1/folder?op=list&authid={0}&path=notexistfolder'.format(answer['authid']))
		answer = req.json()
		self.assertEqual(answer['error_code'], 1151)

	def test023_api_file_upload_1210(self):
		#correctly upload a file by pure post
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		url = 'http://localhost:8000/v1/file?authid={0}&op=upload&filepath=testpost.txt'.format(answer['authid'])
		req = requests.post(url, '123456')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1210)
		
	def test024_api_file_upload_1200(self):
		#correctly upload a file by form post
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		url = 'http://localhost:8000/v1/file?authid={0}&op=upload&filepath=testformpost.txt'.format(answer['authid'])
		headers={'Content-Type':'multipart/form-data'}
		data = b'------WebKitFormBoundaryO3FiuVbj5B5aJbTy\r\nContent-Disposition: form-data; name="xxx"; filename="1.txt"\r\nContent-Type: text/plain\r\n\r\n111\r\n------WebKitFormBoundaryO3FiuVbj5B5aJbTy--\r\n'
		req = requests.post(url, data, headers=headers)
		answer = req.json()
		self.assertEqual(answer['error_code'], 1200)
	
	def test025_api_file_upload_1202(self):
		#upload a exists file(existed at directory)
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		url = 'http://localhost:8000/v1/file?authid={0}&op=upload&filepath=testpost.txt'.format(answer['authid'])
		req = requests.post(url, '123456')
		answer = req.json()
		self.assertEqual(answer['error_code'], 1202)

	def test026_api_file_download_1221(self):#file not exist
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		url = 'http://localhost:8000/v1/file?authid={0}&op=download&filepath=nofile.txt'.format(answer['authid'])
		req = requests.get(url)
		answer = req.json()
		self.assertEqual(answer['error_code'], 1221)
	
	def test027_api_file_download_1220(self):#can get the download short link correctly
		req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
		answer = req.json()
		url = 'http://localhost:8000/v1/file?authid={0}&op=download&filepath=testformpost.txt'.format(answer['authid'])
		req = requests.get(url)
		answer = req.json()
		self.assertEqual(answer['error_code'], 1220)
		