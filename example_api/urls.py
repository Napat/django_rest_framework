from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.PersonList.as_view()),
	# About named regular-expression groups is (?P<name>pattern): https://docs.djangoproject.com/en/1.9/topics/http/urls/#named-groups
	url(r'^age/(?P<age>[0-9]+)/$', views.PersonDetailByAge.as_view()), 		# Try get/put/delete http://127.0.0.1:8000/example_api/age/10/ to manipulate person "age == 10"
	url(r'^name/(?P<name>\w+)/$', views.PersonDetailByName.as_view()), 		# Try get/put/delete http://127.0.0.1:8000/example_api/name/Judy/ to manipulate person "Name == Judy"
	url(r'^hello', views.Hello.as_view(), name="hello"),
    url(r'^world', views.World.as_view(), name="world"),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
