
def create_basic_json_response(error_code, msg, status):
	json_response = {}
	json_response['error_code'] = error_code
	json_response['msg'] = msg
	json_response['status'] = status
	return json_response

def api_file(request):
	'''authid should be validated before this function'''
	response_data = 'file op'
	req_op = request.GET.get('op', '')

	if(request.method == 'POST'):
		if(req_op == 'upload'):
			print(request.body)
			content_type_httpheader = request.META.get('CONTENT_TYPE')#get http header parameter from client
			print(content_type_httpheader)
			if(content_type_httpheader != 'text/plain'):#check if post request from html form element
				print(content_type_httpheader)
				content_type_type = content_type_httpheader.split(';')[0]
				content_type_boundary = content_type_httpheader.split('=')[1]
				print('content_type_type: {0}'.format(content_type_type))
				print('content_type_boundary: {0}'.format(content_type_boundary))
				if(content_type_type == 'multipart/form-data'):#if post request from html form element, the data structure is different from pure post
					response_data = 'post from form'
			else:#if the post request from pure post, the request.body is file content
				response_data = 'post from pure post'
		else:
			response_data = create_basic_json_response(1201, 'not support this op', 'error')
		
	return response_data