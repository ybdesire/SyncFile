import os
import requests
import json

with open('p4vinst64.exe', 'rb') as f:
	url = 'http://localhost:8000/v1/file?authid=3697b250-549b-11e5-a89f-f816546e2287&op=upload&filepath=p4vinst64.exe'
	r = requests.post(url, data=f)
	print(r.json())
