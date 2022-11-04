from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


from . import models
from . import serializers


@api_view(['POST'])
def LoginView(request):
    if request.method == 'POST':
        serializer = serializers.LoginSerializers(data=request.data)
        if serializer.is_valid():
            try:
                queryset = models.CustomUser.objects.get(username=serializer.data['username'])
            except models.CustomUser.DoesNotExist:
                return Response("This username does not exist", status=status.HTTP_404_NOT_FOUND)
            correct_login = serializer.data['password'] == models.CustomUser.objects.get(username=serializer.data['username']).password
            if correct_login:
                response_to_login = {
                    "id": models.CustomUser.objects.get(username=serializer.data['username']).id,
                    "type_of_account": int(models.CustomUser.objects.get(username=serializer.data['username']).type_of_account)
                }
                return Response(response_to_login, status=status.HTTP_200_OK)
            return Response("Incorrect password", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def OneChildrenView(request, id):
    try:
        queryset = models.CustomUser.objects.get(id=id)
    except models.CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        queryset = models.CustomUser.objects.get(id=id)
        serializer_class = serializers.CustomUserSerializers(queryset)
        return Response(serializer_class.data, status=status.HTTP_200_OK)



class RegistrationChildren(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        serializer = serializers.CustomUserRegistrationSerializers(data=request.data)
        if serializer.is_valid():
            try:
                file_obj = request.FILES['profile_pic']
            except:
                file_obj = serializer.data['profile_pic']
            try:
                querysetusername = models.CustomUser.objects.get(username=serializer.data['username'])
            except models.CustomUser.DoesNotExist:
                try:
                    querysetemail = models.CustomUser.objects.get(email=serializer.data['email'])
                except models.CustomUser.DoesNotExist:
                    customUser = models.CustomUser(
                        username=serializer.data['username'],
                        email=serializer.data['email'],
                        name=serializer.data['name'],
                        surname=serializer.data['surname'],
                        password=serializer.data['password'],
                        profile_pic=file_obj,
                        type_of_account=1,
                    )
                    customUser.save()
                    return Response(data="Account created. You can now log in.", status=status.HTTP_201_CREATED)
                return Response(data="This email already exist.", status=status.HTTP_400_BAD_REQUEST)
            return Response(data="This username already exist.", status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
