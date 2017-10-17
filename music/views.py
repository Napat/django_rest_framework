#from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
	all_albums = Album.objects.all()	# Use api to get all object in Album database 
	return render(request, 'music/index.html', {'all_albums': all_albums,})		

	#### same as
	# all_albums = Album.objects.all()	# Use api to get all object in Album database 
	# template = loader.get_template('music/index.html')
	# context = {
	# 	'all_albums': all_albums,
	# }
	# return HttpResponse(template.render(context, request))

def detail(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/detail.html', {'album': album})	

	#### same as
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# except Album.DoesNotExist:
	# 	raise Http404("No Album matches the given query")
	# return render(request, 'music/detail.html', {'album': album})	