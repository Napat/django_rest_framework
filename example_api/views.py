from django.shortcuts import render

# Create your views here.
from django.utils.encoding import force_text
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.parsers import JSONParser
from rest_framework import mixins
from rest_framework import generics

import json

from .models import Person
from .serializers import PersonSerializer

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

class PersonList(APIView):
    """
    List all persons, or create a new person.
    """
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetailByAge(APIView):
    """
    Retrieve, update(by put) or delete a person instance.
    """
    def get_object(self, age):
        try:
            return Person.objects.get(age=age)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, age, format=None):
        try: 
            person = self.get_object(age)
        except Person.MultipleObjectsReturned:
            person = {"detail":"MultipleObjectsReturned"}
            return Response(person, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

        person = self.get_object(age)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, age, format=None):
        person = self.get_object(age)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, age, format=None):
        person = self.get_object(age)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PersonDetailByName(APIView):
    """
    Retrieve, update(by put) or delete a person instance.
    """
    def get_object(self, name):
        try:
            return Person.objects.get(name=name)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        try: 
            person = self.get_object(name)
        except Person.MultipleObjectsReturned:
            person = {"detail":"Dataase error MultipleObjectsReturned"}
            return Response(person, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  

        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        person = self.get_object(name)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        person = self.get_object(name)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 