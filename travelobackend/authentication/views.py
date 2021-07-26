from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import User
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from authentication.serializers import UserAuthSerializer
from django.core.validators import validate_email


@api_view(['GET'])
def register(request):
    data = request.data
    username = data.get('username')
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    email_valid_check_result = validate_email(email)
    messages = {'errors': []}

    if username == None:
        messages['errors'].append('username can\'t be empty')
    if email == None:
        messages['errors'].append('Email can\'t be empty')
    if name == None:
        messages['errors'].append('Name can\'t be empty')
    if not email_valid_check_result == email:
        messages['errors'].append(email_valid_check_result)
    if password == None:
        messages['errors'].append('Password can\'t be empty')
    if User.objects.filter(email=email).exists():
        messages['errors'].append("Account already exists with this email id.")
    if User.objects.filter(username__iexact=username).exists():
        messages['errors'].append("Account already exists with this username.")

    if len(messages['errors']) > 0:
        return Response({"detail": messages['errors']}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create(
            username=username,
            email=email,
            name=name,
            password=make_password(password)
        )
        serializer = UserAuthSerializer(user, many=False)
    except Exception as e:
        return Response({'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data)
