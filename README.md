SyncFile
===================


SyncFile is developed for file sync across all platforms.
Currently, the API development is in progress.

----------

> **Note:**

> - Developed by python 3.4.3 and Django 1.8.2.
> - Local storage path 'base_dir' could be modified at file_manage.py at 'curr_path = str(os.path.dirname(os.path.realpath(__file__)))' as __file__.

Completed API
------------------
## <i class="icon-pencil"></i> Auth

###**userRegister**
######API
http://localhost:8000/v1/userRegister?username=user&password=password&email=user@email.com
######Response
| error_code| status| msg   |
| :------- | :---- | :------- |
| 1000    | success   |  registered a new user.   |
| 1001    | error   |  the user has been registered, please change the user name   |
| 1002    | error   |  the email has been registered, please change the email   |
| 1003    | error   |  blank username/password/email   |
| 1004    | error   |  username cannot contain the following characters: \/:*?"<>|   |

###**getAuthID**
######API
http://localhost:8000/v1/getAuthID?fmt=json&username=user1&password=password
######Response
| error_code| authid | status | msg   |
| :------- | :---- | :---- |:------- |
| 1010     | 'xoxo'| success |  auth id get ok   |
| 1011     | ' '   | error |  auth failure. user is not registered or user name/password incorrect   |

###**isAuthAlive**
######API
http://localhost:8000/v1/isAuthAlive?authid=xxxooo
######Response
| error_code| auth_time | status   | msg  |
| :------- | :----------| :------- | :------- |
| 1020     |  auth time UTC  | success  |  valid authid, and auth still alive   |
| 1021     |  ' '            |  error |   invalid authid   |

###**folder?op=mkdir**
######API
http://localhost:8000/v1/folder?op=mkdir&authid=xxxooo&path=book
######Response
| error_code | status   | msg  |
| :------- | :------- | :------- |
| 1100     |   success  |  folder created successfully   |
| 1101     |   error |   folder already exist   |
| 1102     |   error |  folder path should not ended with \    |
| 1103     |   error |  folder path error. the parent folde should be created firstly. and use \    |

###**folder?op=getdetail**
######API
http://localhost:8000/v1/folder?op=getdetail&authid=xxx&path=testdir
######Response
| error_code | status   | msg  |  details |
| :------- | :------- | :------- | :------- |
| 1120     |   success  |  folder details info  | id, parentid, type, size, createdate, creator, filename, foldername, path |
| 1121     |   error |   foler not exist. please check path format & content   | '' |


###**folder?op=rename**
######API
http://localhost:8000/v1/folder?op=rename&authid=xxx&path=xxx&name=xxx
######Response
| error_code | status   | msg  |
| :------- | :------- | :------- |
| 1130     |   success  |  renamed folder {0} to {1}   |
| 1131     |   error    |  requested folder not exist   |


###**folder?op=list**
######API
http://localhost:8000/v1/folder?op=list&authid=xxx&path=xxx
######Response
| error_code | status   | msg  |
| :------- | :------- | :------- |
| 1150     |   success  |  get folder list   |
| 1151     |   error    |  requested folder not exist. or path format error(use /)   |


###**file?op=upload**
File could be uploaded by pure POST(from python) and form POST(from html).
######API
POST http://localhost:8000/v1/file?authid={0}&op=upload&filepath=testpost.txt
filepath include the file name and file path.
######Response
| error_code | status   | msg  |
| :------- | :------- | :------- |
| 1200    |   success   |   file uploaded by form successfully  |
| 1210    |   success   |   file uploaded by POST successfully  |
| 1201    |   error  |  not support this op(POST only support op=upload)   |
| 1202    |   error  |  file already exist at server dir   |
| 1203    |   error  |  file creation exception(pure OST)    |
| 1204    |   error  |  file creation exception(form POST)   |
| 1205    |   error  |  file already exist at DB   |
| 1206    |   error  |  Incorrect API format, please check manual   |


###**file?op=download**
File download should be requested 2 times. First request the API below, and get a short link for file download. And send the second request to the short link can download a file.
######API
http://localhost:8000/v1/file?authid={0}&op=download&filepath=testformpost.txt
success return like this: {"error_code": 1220, "msg": "localhost:8000/v1/f?id=b3e75ec0-5cde-11e5-acbc-ea9f05b65156", "status": "success"}
######Response
| error_code | status   | msg  |
| :------- | :------- | :------- |
| 1220    |   success   |   short link  |
| 1221    |    error    |   file not exists  |
| 1222    |    error    |   server busy, repeat again  |
