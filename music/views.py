###############################################################
# Using django generic views
###############################################################
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.views.generic import View 

from .models import Album 
from .forms import UserForm

# generic.ListView: to view the list of objects
class IndexView(generic.ListView):
	template_name = 'music/index.html' # plugin template
	context_object_name = 'all_albums' # overide default get_queryset return variable name: 
									   # 'object_list' to 'all_albums' that pass to template_name('music/index.html') 

	def get_queryset(self):
		return Album.objects.all()

# generic.DetialView: to view details of one object
class DetailView(generic.DetailView):
	template_name = 'music/detail.html' # plugin template
	model = Album 						# set object type for handler  
 	
# CreateView: class to create form for new object(ie: Album object)
class AlbumCreate(CreateView):
	model = Album 
	fields = ['artist', 'album_title', 'genre', 'album_logo']

# UpdateView: class to create form for update object(ie: Album object)
class AlbumUpdate(UpdateView):
	model = Album 
	fields = ['artist', 'album_title', 'genre', 'album_logo']

# DeleteView: class to Delete object handler
class AlbumDelete(DeleteView):
	model = Album 
	success_url = reverse_lazy('music:index')	# redirect to music/index page if success deleted

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html' 

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data: write data(from POST) to database
	def post(self, request):
		# get data that user input to form and POST
		form = self.form_class(request.POST)

		if form.is_valid():
			# storing to local object variable(user) but still NOT save to database yet
			user = form.save(commit=False)	

			# cleaned(normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)		# replace password have to call set_password()

			user.save()

			# return User objects if credentials are corrent
			user = authenticate(username=username, password=password)

			if user is not None:
				# check user is not in banned list
				if user.is_active:
					login(request, user)
					return redirect('music:index')

		# something is wrong! return blank form to user
		return render(request, self.template_name, {'form': form})

# ###############################################################
# Deplicate code: Only for understand detail
# ###############################################################
# #from django.http import Http404
# #from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from .models import Album
#
# def index(request):
# 	all_albums = Album.objects.all()	# Use api to get all object in Album database 
# 	return render(request, 'music/index.html', {'all_albums': all_albums,})		
#
# 	#### same as
# 	# all_albums = Album.objects.all()	# Use api to get all object in Album database 
# 	# template = loader.get_template('music/index.html')
# 	# context = {
# 	# 	'all_albums': all_albums,
# 	# }
# 	# return HttpResponse(template.render(context, request))
#
# def detail(request, album_id):
# 	album = get_object_or_404(Album, pk=album_id)
# 	return render(request, 'music/detail.html', {'album': album})	
#
# 	#### same as
# 	# try:
# 	# 	album = Album.objects.get(pk=album_id)
# 	# except Album.DoesNotExist:
# 	# 	raise Http404("No Album matches the given query")
# 	# return render(request, 'music/detail.html', {'album': album})	
#
# def favorite(request, album_id):
# 	album = get_object_or_404(Album, pk=album_id)
# 	try:
# 		select_song = album.song_set.get(pk=request.POST['song'])
# 	except (KeyError, Song.DoesNotExist):
# 		return render(request, 'music/detail.html',
# 							{
# 								'album': album,
# 								'error_message': "You did not select a valid song",
# 							}
# 						)
# 	else:
# 		select_song.is_favorite = not select_song.is_favorite	# toggle
# 		select_song.save()
# 		return render(request, 'music/detail.html', {'album': album})
#
