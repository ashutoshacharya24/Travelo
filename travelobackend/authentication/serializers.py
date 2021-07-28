from django.db.models import fields
from users.models import User
from rest_framework import serializers


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name']
