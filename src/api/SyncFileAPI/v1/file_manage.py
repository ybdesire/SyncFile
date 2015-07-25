import os

class fileManage:
	def __init__(self, basedir=''):
		self.base_dir = os.getcwd() + '\\userdata\\'
	
	def create_folder(self, path):
		try:
			os.mkdir(self.base_dir + path)
		except Exception as e:
			print(e)
	
	def fun(self):
		print('xxx: {0}'.format(self.base_dir))
		
def main():
	mgr = fileManage()
	mgr.create_folder(r'user1')
	mgr.fun()
		
if __name__=='__main__':
	main()