import os
import shutil

class fileManage:
	'''parameters
		basedir: 	absolute path for data storage. such as 'c:\\userdata'
		path:		relative path. such as 'user1\\ooo'
	'''
	def __init__(self, basedir=''):
		curr_path = str(os.path.dirname(os.path.realpath(__file__)))
		self.base_dir =  os.path.join(curr_path,'userdata')
	
	'''create folder at relative path, the uplevel folder should exist'''
	def create_folder(self, path):
		try:
			complete_path = os.path.join(self.base_dir, path)
			print('Create folder at: {0}'.format(complete_path))
			os.mkdir('{0}'.format(complete_path))
			return True,''
		except Exception as e:
			return False, e
	
	'''delete all files and folders under path, include the dir at path level'''
	def delete_folder(self, path):
		try:
			full_path = os.path.join(self.base_dir, path)
			shutil.rmtree(full_path)
			return True, ''
		except Exception as e:
			return False, e
	
	'''rename a folder's name'''
	def rename_folder(self, path, name):
		try:
			full_path_src = os.path.join(self.base_dir, path)
			full_path_dst = os.path.join(self.base_dir, os.path.split(path)[0], name)
			os.rename(full_path_src, full_path_dst)
			return True, ''
		except Exception as e:
			return False, e		
	
	def is_exists(self, path):
		full_path = os.path.join(self.base_dir, path)
		return os.path.exists(full_path)
		
	def create_file(self, filepath, filedata):
		try:
			full_file_path = os.path.join(self.base_dir, filepath)
			if os.path.exists(full_file_path):
				return False, 'file already exists'
			else:
				file = open(full_file_path, 'wb+')#write bytes to file
				file.write(filedata)
				file.close()
				return True, ''
		except Exception as e:
			return False, e		
			
	def get_file_data(self, filepath):
		try:
			full_file_path = os.path.join(self.base_dir, filepath)
			if not os.path.exists(full_file_path):
				return False, 'file not exists'
			else:
				file = open(full_file_path, 'rb')#read file as bytes
				return True, file.read()
		except Exception as e:
			return False, e
def test():
	mgr = fileManage()
	#stat = mgr.delete_folder(r'user1\kkk')
	stat = mgr.create_file('testuser1\\book\\code\\1.txt', b'123456'[2:])
	if stat[0]:
		print('success')
	else:
		print(stat[1])
		
if __name__=='__main__':
	test()