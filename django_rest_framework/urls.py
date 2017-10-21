"""django_rest_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from auth import views as authviews
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', authviews.UserViewSet)
router.register(r'groups', authviews.GroupViewSet)

urlpatterns = [
    # 'r' : regular expression
    # '^' : beginning
    # '$' : ending 
    # so r'^$' means when requested to individual app path, for example, 
    # http://127.0.0.1:8000/
	url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
    url(r'^example_api/', include('example_api.urls')),
    url(r'^samplepage/', include('samplepage.urls')),
    url(r'^music/', include('music.urls')),
]

# if debug mode(developer env)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

