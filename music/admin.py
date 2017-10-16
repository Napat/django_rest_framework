from django.contrib import admin
from .models import Album, Song

admin.site.register(Album) # register Album to admin GUI management: http://127.0.0.1:8000/admin/
admin.site.register(Song) # register Song to admin GUI management: http://127.0.0.1:8000/admin/
