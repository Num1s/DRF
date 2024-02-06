from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Confirm
from .serializers import UserCreateSerializer, UserAuthSerializer, UserConfirmSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import random

# Create your views here.

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.create_user(username=username, password=password, is_active=False)
    confirm = Confirm.objects.create(user=user, code=random.randint(100000, 999999))

    return Response(data={'code': confirm.code}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        try:
            token = Token.objects.get(user=user)
        except:
            token= Token.objects.create(user=user)
        return Response(data={'key': token.key})
    
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def confirm_api_view(request):
    serializer = UserConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = User.objects.get(username=username)
    if user:
        confirm = Confirm.objects.get(user=user)
        if confirm.code == serializer.validated_data.get('code'):
            user.is_active = True
            user.save()
            return Response(data={'accepted': 'Success!'}, 
                            status=status.HTTP_200_OK)
    else:
        return Response(data={'error': 'This user does not exists!'}, 
                    status=status.HTTP_404_NOT_FOUND)
        