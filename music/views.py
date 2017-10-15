from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>This is the music app homepage</h1>")

def detail(request, album_id):
	return HttpResponse(f"<h2>Details for Album id: {album_id}</h2>")
