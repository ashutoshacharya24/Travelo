from django.db.models import fields
from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'profile', 'is_active', 'is_admin', 'last_login']
