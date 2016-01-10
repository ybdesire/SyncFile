# Environment introduction
## API side:
1. OS: Windows Server 2008 R2
2. python 3.4.3
3. Django 1.8.2  (pip install django==1.8.2)
4. other: 
   * notepad++, pip
   * requests-2.7.0-py2.py3-none-any.whl(pip install requests)
   * pytz(version2015.4)#pip install pytz
   * follow the url below to install django-cors-headers and set settings.py

		http://stackoverflow.com/questions/22476273/no-access-control-allow-origin-header-is-present-on-the-requested-resource-i
      * pip install django-cors-headers


## UI side:
1. Install nodejs v4 or v5
2. $ npm update
3. Install bower for global environment
    $ npm install -g bower


# Environment setup

## For Linux

I guess pip is install at your local machine if not then do:

``` sh
(For Debian based machine)
sudo apt-get install python-pip
```

``` sh
pip install virtualenv
virtualenv <folder-name>
```

Change the directory to folder which you have created
``` sh
source bin/activate
```

Then clone the repositry and move to folder codejudge and follow these steps:
``` sh
pip install -r requirements.txt
```

## For Windows

Setup virtualenv and install the dependences.
