from django.db import models

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=1000)

class Song(models.Model):
	# ForeignKey: link Song to Album database index
	# models.CASCADE: when delete Album then delete Song that linked to that Album 
	album = models.ForeignKey(Album, on_delete=models.CASCADE)	
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)
