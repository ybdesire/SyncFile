import os
import requests
import json

with open('1.txt') as f:
	text = f.read()
	url = 'http://localhost:8000/v1/file?authid=8178e4ee-4c84-11e5-b640-ea9f05b65156&op=upload'
	data = json.dumps({'file_name':'1.txt', 'data':text})
	r = requests.post(url, data)
	print(r.json())
