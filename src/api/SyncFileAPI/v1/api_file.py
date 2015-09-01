from . import file_manage
from .models import UserAuthID, FileSys

def create_basic_json_response(error_code, msg, status):
	json_response = {}
	json_response['error_code'] = error_code
	json_response['msg'] = msg
	json_response['status'] = status
	return json_response

def upload_file(request):
	req_auth_id = request.GET.get('authid', '')
	req_username = UserAuthID.objects.filter(authID = req_auth_id)[0].userName
	req_file_path = request.GET.get('filepath', '')
	file_path = '{0}\\{1}'.format(req_username, req_file_path)
	
	mgr = file_manage.fileManage()
	
	#print(request.body)
	content_type_httpheader = request.META.get('CONTENT_TYPE')#get http header parameter from client
	#print(content_type_httpheader)
	if(content_type_httpheader != 'text/plain'):#post request from html form element
		#print(content_type_httpheader)
		content_type_type = content_type_httpheader.split(';')[0]
		content_type_boundary = content_type_httpheader.split('=')[1]
		#file_data = request.body.split('\r\n\r\n')[1]
		#print(file_data)
		#print('content_type_type: {0}'.format(content_type_type))
		#print('content_type_boundary: {0}'.format(content_type_boundary))
		response_data = 'post from form'
		#stat = mgr.create_file(file_path, )
	else:#if the post request from pure post, the request.body is file content
		response_data = 'post from pure post'
	return response_data
	
def api_file(request):
	'''authid should be validated before this function'''
	response_data = 'file op'
	req_op = request.GET.get('op', '')
	req_file_path = request.GET.get('filepath', '')
	print(req_file_path)
	if(request.method == 'POST'):
		if(req_op == 'upload'):
			response_data = upload_file(request)
		else:
			response_data = create_basic_json_response(1201, 'not support this op', 'error')
		
	return response_data