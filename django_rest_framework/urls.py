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
from rest_framework import routers
from example_api import views as example_apiviews

router = routers.DefaultRouter()
router.register(r'users', example_apiviews.UserViewSet)
router.register(r'groups', example_apiviews.GroupViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
    url(r'^example_api/hello', example_apiviews.Hello.as_view(), name="hello"),
    url(r'^example_api/world', example_apiviews.World.as_view(), name="world"),	
	url(r'^admin/', admin.site.urls),
]
