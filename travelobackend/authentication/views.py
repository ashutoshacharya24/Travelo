from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from authentication.serializers import UserAuthSerializer
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login, logout


@api_view(['POST'])
def register_view(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    messages = {'errors': []}

    if username == None:
        messages['errors'].append('username can\'t be empty')
    if email == None:
        messages['errors'].append('Email can\'t be empty')
    if name == None:
        messages['errors'].append('Name can\'t be empty')
    if password == None:
        messages['errors'].append('Password can\'t be empty')

    if User.objects.filter(email=email).exists():
        messages['errors'].append("Account already exists with this email id.")
    if User.objects.filter(username__iexact=username).exists():
        messages['errors'].append("Account already exists with this username.")

    if len(messages['errors']) > 0:
        return Response({"detail": messages['errors']}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create(username=username, email=email, name=name, password=make_password(password))
        serializer = UserAuthSerializer(user, many=False)
    except Exception as e:
        return Response({'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)


@api_view(['POST'])
def login_view(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if '@' in username:
        kwargs = {'email': username}
    else:
        kwargs = {'username': username}

    try:
        user = User.objects.get(**kwargs)
        if user.check_password(password):
            serializer = UserAuthSerializer(user, many=False)
            login(request, user)
    except User.DoesNotExist:
        return Response({'detail': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)


@api_view(['GET'])
def logout_view(request):
    logout(request)
    return Response({'detail': 'Logout success'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def me(request):
    if request.user.is_authenticated:
        serializer = UserAuthSerializer(request.user)
        return Response({'detail': 'User is authenticated', 'user': serializer.data})
    else:
        return Response({'detail': 'Authentication not found'}, status=status.HTTP_400_BAD_REQUEST)
