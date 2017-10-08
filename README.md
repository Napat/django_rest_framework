References  
- [quickstart](http://www.django-rest-framework.org/tutorial/quickstart/)  

Test with python 3.6.3  

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
`http://localhost:8000`   
`http://localhost:8000/admin`   
`http://127.0.0.1:8000/appapi01/hello`  
`http://127.0.0.1:8000/appapi01/hello?format=json`  
  
Try Chrome's extension “Advanced Rest Client” to api server:  
`http://127.0.0.1:8000/appapi01/hello`   
  
- Adding Authorization at `Headers form`   
`https://stackoverflow.com/questions/20591770/how-to-test-rest-api-using-chromes-extension-advanced-rest-client`  

```
Authorization / Basic YWRtaW46cGFzc3dvcmQxMjM=  
```
  
GET should receive json `{"hello": "world"}`  
POST Raw payload: `hello=worldworldworld`    

