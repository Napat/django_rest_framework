
# Basic models and database

## To migrate database when change models.py
```
## creating new migrations
python manage.py makemigrations music

## displays the SQL statements for a migration
python manage.py sqlmigrate music 0001

## applying migrations to database
python manage.py migrate
```

## Django database shell(Python shell with Django database command)  
```
## Open Django database api shell and input some database commands
python manage.py shell
---------------------------------------------------
Python 3.6.3 (default, Oct  6 2017, 18:47:46)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
>>> from music.models import Album, Song
>>> Album.objects.all()
<QuerySet []>
>>>
>>> a = Album(artist="Taylor Swift", album_title="Red", genre="Country", album_logo="https://upload.wikimedia.org/wikipedia/en/e/e8/Taylor_Swift_-_Red.png")
>>> 
>>> a.save()
>>> a.id
1
>>> a.pk    # primary key is the same as a.id 
1
>>> a.artist
'Taylor Swift'
>>> Album.objects.all()
<QuerySet [<Album: Album object>]>
>>>
>>> b = Album()
>>> b.artist = "X Japan"
>>> b.album_title = "Blue Blood"
>>> b.genre = "heavy metal"
>>> b.album_logo ="https://upload.wikimedia.org/wikipedia/en/a/a2/X_Japan_-_Blue_Blood.jpg" 
>>> b.id
>>> b.save()
>>> b.id
2
>>>
>>> Album.objects.all()
<QuerySet [<Album: Album object>, <Album: Album object>]>
>>> 
>>> exit()
```

## To set string represent the Album object, we need to create string dunder method.  
``` 
# Set string dunder object
class Album(models.Model):
    ...
    def __str__(self):
        return self.album_title + ' - ' + self.artist
    ...
```

## Test string dunder of Album  
```
python manage.py shell
>>> from music.models import Album, Song
>>> Album.objects.all()
<QuerySet [<Album: Red - Taylor Swift>, <Album: Blue Blood - X Japan>]>
>>> 
>>> Album.objects.filter(id=2)
<QuerySet [<Album: Blue Blood - X Japan>]>
>>> 
>>> Album.objects.filter(id=3)
<QuerySet []> 
>>> 
>>> Album.objects.filter(artist__startswith='X')
<QuerySet [<Album: Blue Blood - X Japan>]>
>>> 
```

## Adding object1 that has relationship with object2 using shell(Song --> Album)  

Open python shell with Django  
```
python manage.py shell
---------------------------------------------------
```

- Method 1: Create Song object and set reference to Album object  
```
>>> from music.models import Album, Song
>>> album1 = Album.objects.get(pk=1)        # get object with primary key= 1
>>> album1.artist  
'Taylor Swift'
>>> song = Song()                           # New object
>>> song.album = album1 
>>> song.file_type = 'mp3'
>>> song.song_title = 'Begin Agirl'         # With misspell
>>> song.save()
>>>
############################################## 
### Try http://127.0.0.1:8000/admin/music/song/  
### and notice missspell
############################################## 
>>> song.song_title = 'Begin Again'         # To change 
>>> song.save()
############################################## 
### Try http://127.0.0.1:8000/admin/music/song/  
############################################## 
```

- Method 2: Using related objects set   
```
>>> album1.song_set.count()
1
>>> song2 = album1.song_set.create(song_title='Red',file_type='mp3')
>>> song3 = album1.song_set.create(song_title='Treacherous',file_type='mp3')
>>> song4 = album1.song_set.create(song_title='I Knew You Were Trouble',file_type='mp3')
>>> song5 = album1.song_set.create(song_title='All Too Well',file_type='mp3')
>>> song4.song_title
'I Knew You Were Trouble'
>>> album1.song_set.count()
5
############################################## 
### Try http://127.0.0.1:8000/admin/music/song/  
############################################## 
```
