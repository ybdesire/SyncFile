
def API_folder(request):
	req_op = request.GET.get('op', '')
	
	
	return req_op