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


