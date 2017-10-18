from django.conf.urls import url
from . import views

app_name = 'music'	# namespace of this urls.py

urlpatterns = [
	# /music/ :this is default homepage(index)
	url(r'^$', views.index, name="index"),		

	# /music/<album_id>/ :when <album_id> represent album_id that is a number ie: 1, 2, 500
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), 

	# /music/<album_id>/favorite/ 
	url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'), 
]
