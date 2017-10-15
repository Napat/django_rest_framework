
# To migrate database when change models.py
```
## creating new migrations
python manage.py makemigrations music

## displays the SQL statements for a migration
python manage.py sqlmigrate music 0001

## applying migrations to database
python manage.py migrate
```

# Django database shell(Python shell with Django database command)  
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
>>> 
```
