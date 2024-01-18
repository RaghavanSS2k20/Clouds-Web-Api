from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from web.models import WebUser
from web.serializers import WebUserSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def addUser(request):
    data = JSONParser().parse(request)
    data_ser = WebUserSerializer(data=data)
    if data_ser.is_valid():
        data_ser.save()
        return JsonResponse(data_ser.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(data_ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def index(request):
    return JsonResponse({"message":'working'}, status= status.HTTP_200_OK)
# Create your views here.
