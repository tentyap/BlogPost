import base64
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import User 

from rest_framework.decorators import APIView
from rest_framework.authtoken.models import Token
# from restapp import global_msg
from rest_framework import status
from .serializers import UserRegistrationSerializer


def login_data(request):
    error_list=[]
    auth_headers=request.META['HTTP_AUTHORIZATION']#Basic ykjfksdkf
    encoded_data=auth_headers.split(' ')[1]
    decoded_data= base64.b64decode(encoded_data).decode('utf-8').split(":")#["username" : "password"]
    user_name=decoded_data[0]
    password=decoded_data[1]
    print(password)
    if user_name and password:#checking user name and password if blank
        user=User.objects.filter(username=user_name)#user x ki xoina vanara check garni  yedi user ="kamal" x vani
        if user.exists():#yaha aaux
            user=user.first()
            db_password=user.password#user name  "kamal " ko password aux 
            is_match_password=check_password(password,db_password)#checck password of database and user le hanako
            if not is_match_password:
                error_list.append("invalid username and password") 
            else:
                print(user_name)   
        else:
              error_list.append("no such user in database")
    else:
        error_list.append("username and password cannot be blank")
    return error_list,user_name,password

class LoggingApiView(APIView):
    authentication_classes=[]
    permission_classes=[]
    
    def post(self,request):
        print(request.data)
        error_list,user_name,password1=login_data(request)
        if error_list:
            msg={
            "errors":error_list
            }
            return JsonResponse(msg, status = 404)
        user=authenticate(request,username=user_name, password=password1)#aagadi ko databse pachdai ko user ko password ho
        if user is not None:
            token, created=Token.objects.get_or_create(user=user)
            msg={
                "username":user.username,
                "email":user.email,
                "token":token.key
            }
            return JsonResponse(msg, status=200)
        return JsonResponse({'msg':"ok"},status=200)
    

class UserRegisterApiView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg': 'User registered successfully'}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error': 'Internal server error', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
