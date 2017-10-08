from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from example_api.serializers import UserSerializer, GroupSerializer

from django.utils.encoding import force_text
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse

import json
import math

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
   
class Hello(APIView):
    def get(self, request, *args, **kw):
        print("calling get method of Hello")
        # Any URL parameters get passed in **kw
        result = {"hello": "123456"}
        response = Response(result, status=status.HTTP_200_OK)
        return response

    def post(self, request, *args, **kw):
        print("calling post method of Hello")
        data = request.data
        pred = data
        result = {"result": pred}
        response = Response(result, status=status.HTTP_200_OK)
        return response  		

class World(APIView):
    def get(self, request, *args, **kw):
        temp_val = '+40C'
        html_ = f'''
                <!DOCTYPE html>
                <html lang=en>
                 <head>
                 </head>
                 <body>
                  <h1>My World!</h1>
                  <p>Temp: {temp_val} is very hot</p>
                </body>
                </html>'''        
        return HttpResponse(html_)

    # need to input
    def post(self, request, *args, **kw):
        print("calling post method of Hello")
        body_unicode = request.body.decode('utf-8')
        #print(body_unicode)
        try:
        	body = json.loads(body_unicode)
        except:
        	print(f"Bad json input: {body_unicode}")
        	result = {}
        	return Response(result, status=status.HTTP_400_BAD_REQUEST)

        try:
        	q_str = body['q']        	
        except:
        	print(f"Bad json input: {body_unicode}")
        	result = {}
        	return Response(result, status=status.HTTP_400_BAD_REQUEST)

        print(f"query string: ____{q_str}....")
        output = f"{q_str} is your query string"
        result = {"result": output}
        response = Response(result, status=status.HTTP_200_OK)
        return response 
