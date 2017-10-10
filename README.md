References  
- [quickstart](http://www.django-rest-framework.org/tutorial/quickstart/)  
- [status code](http://www.django-rest-framework.org/api-guide/status-codes/)  

Requirement
- python 3.6.x because 'String Interpolation' syntax [More](https://www.python.org/dev/peps/pep-0498/)    

Project นี้ถูกสร้างด้วยขั้นตอนคร่าวๆดังนี้  
```
# Create project
$ django-admin.py startproject django_rest_framework
$ cd django_rest_framework

# Create new app  
$ django-admin.py startapp example_api

# Edit some config(see reference quickstart for more information)
...

```

สามารถเริ่มต้นใช้งานโปรเจคนี้ได้ดังนี้  
```
# Clone project
$ git clone <...project url...>

# Create virtualenv and activated
$ virtualenv venv_bashp36 
$ source venv_bashp36/bin/activate

# Install python module
$ pip install -r requirements.txt
```

การใช้งานครั้งแรกจะต้องทำการ migrate database คำสั่งดังนี้  
```
# First time only: Create database and user/password: 'admin'/'password123'
$ python manage.py migrate
$ python manage.py createsuperuser
```
  
More about database config: `site_projectcfg/setting.py` > `DATABASES = {...}`
  
Run Server    
```
$ python manage.py runserver
```
  
Try (ต้อง login ด้วยนะ)  
```
# GET
http://localhost:8000
http://localhost:8000/admin

http://127.0.0.1:8000/example_api/

## Should see {"hello": "world"} 
http://127.0.0.1:8000/example_api/hello          

## Should see {"hello": "world"} 
http://127.0.0.1:8000/example_api/hello?format=json

http://127.0.0.1:8000/example_api/world
```

Try  
```
# POST

## POST Raw payload(Method type=application/x-www-form-urlencoded)
## Content: `foo=bar`  
## Should see {"result": {"foo": "bar"}}
http://127.0.0.1:8000/example_api/hello 

```

Try  
1. Chrome's extension “Advanced Rest Client” to api server:  
`http://127.0.0.1:8000/example_api/hello`   
2. Adding Authorization at `Headers form`   
`https://stackoverflow.com/questions/20591770/how-to-test-rest-api-using-chromes-extension-advanced-rest-client`  
Example:  
```
Authorization / Basic YWRtaW46cGFzc3dvcmQxMjM=  
```
3. test GET and POST method  
4. Try POST to `http://127.0.0.1:8000/example_api/world` with  
```
## 4.1 Raw header: {"q":"world"}
### Should see 200 OK with json:
{ "result": "world is your query string"}

## 4.2 Raw header: {"hello"="world"}
### Should see 400 Bad Request with json:
{}

```


