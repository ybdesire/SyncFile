import os
import requests
import json

try:
    req = requests.get('http://localhost:8000/v1/getAuthID?username=testuser1&password=123')#exist username & password
    answer = req.json()
    print(answer['authid'])
    with open('p4vinst64.exe', 'rb') as f:
            url = 'http://localhost:8000/v1/file?authid={0}&op=upload&filepath=p4vinst64.exe'.format(answer['authid'])
            r = requests.post(url, data=f)
            if(r.status_code==500):
                with open('l.html', 'wb+') as fo:
                    fo.write(r.content)
            else:
                print(r.json())
except Exception as e:
    print(e)
