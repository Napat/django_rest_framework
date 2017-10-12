from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.PersonList.as_view()),
	url(r'^age/(?P<age>[0-9]+)/$', views.PersonDetailByAge.as_view()), 	# Try get/put/delete http://127.0.0.1:8000/example_api/age/10/ to manipulate person that "age == 10"
	url(r'^hello', views.Hello.as_view(), name="hello"),
    url(r'^world', views.World.as_view(), name="world"),    
]

urlpatterns = format_suffix_patterns(urlpatterns)
