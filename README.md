SyncFile
===================


SyncFile is developed for file sync across all platforms.
Currently, the API development is in progress.

----------

> **Note:**

> - Developed by python 3.4.3 and Django 1.8.2.
> - Please config the 'base_dir' at file_manage.py firstly, which is for user file/folder storage path at server.

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
| 1011     | ' '   | error |  auth failure. user is not registed or user name/password incorrect   |

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