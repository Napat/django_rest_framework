
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

