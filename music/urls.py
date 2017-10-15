from django.conf.urls import url
from . import views

urlpatterns = [
	# /music/ ,this is default homepage(index)
	url(r'^$', views.index, name="index"),		

	# /music/nnn/ ,when nnn represent album_id that is a number ie: 1, 2, 500
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), 
]
