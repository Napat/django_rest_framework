from django.db import models
from django.core.urlresolvers import reverse 

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.FileField(max_length=1000)		# FileField to keep files

	# method for CreateView
	def get_absolute_url(self):
		print(f"....CreateView at primary key: {self.pk}....")
		# pass primary key to detail page 
		return reverse('music:detail', kwargs={'pk': self.pk}) 

	# str dunder"(double underscore) methods: 
	# represent to string of this object
	def __str__(self):
		return self.album_title + ' - ' + self.artist

class Song(models.Model):
	# ForeignKey: link Song to Album database index
	# models.CASCADE: when delete Album then delete Song that linked to that Album 
	album = models.ForeignKey(Album, on_delete=models.CASCADE)	
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)
	is_favorite = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.song_title}.{self.file_type} / {self.album.artist}"