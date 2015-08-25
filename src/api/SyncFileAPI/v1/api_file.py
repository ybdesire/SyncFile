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
			response_data = 'upload'
		else:
			response_data = create_basic_json_response(1201, 'not support this op', 'error')
		
	return response_data