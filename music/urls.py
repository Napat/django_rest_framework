from django.conf.urls import url
from . import views

app_name = 'music'	# namespace of this urls.py


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="index"),	

	# 
	url(r'^register/$', views.UserFormView.as_view(), name="register"),	

	# /music/2/ 	album detail page id 2	
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), 

	# /music/album/add/ 	to create album
	url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'), 

	# /music/album/2/ 		to update album id 2
	url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'), 

	# /music/album/2/delete/ to delete album id 2
	url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'), 		
]


# ###############################################################
# Deplicate code: Only for understand detail
# ###############################################################
# urlpatterns = [
# 	# /music/ :this is default homepage(index)
# 	url(r'^$', views.index, name="index"),		
#
# 	# /music/<album_id>/ :when <album_id> represent album_id that is a number ie: 1, 2, 500
# 	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), 
#
# 	# /music/<album_id>/favorite/ 
# 	url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'), 
# ]
