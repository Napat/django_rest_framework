from django.contrib import admin
from .models import Album

# register Album to admin GUI management: http://127.0.0.1:8000/admin/
admin.site.register(Album)
