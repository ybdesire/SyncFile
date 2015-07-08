v1 API is for http/https API. RestAPI should be implemented in future version(v2 or latter).

## Request
* http://url/v1/method?[parameter collection]

## Response
* &fmt=json
* &fmt=jsonp along with an optional callback: &jsonp_callback=callbackname
* &fmt=xml

## General API Methods
### methods

#### folder
* http://url/v1/folder
* 
#### file
* http://url/v1/file
* 
#### user
* http://url/v1/user
* 
#### group
* http://url/v1/group
* 
#### search
* http://url/v1/search


## Restriction
* v1 API support only SQLite
* v1 API support only json response
* v1 API do not care much about security
