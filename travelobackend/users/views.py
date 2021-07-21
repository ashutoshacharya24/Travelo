from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import permissions
from users.models import User
from users.serializers import ProfileSerializer
from users.permissions import IsOwner


class UserProfileView(RetrieveAPIView):
    queryset = User.active.all()
    serializer_class = ProfileSerializer


class UserProfileUpdateView(UpdateAPIView):
    queryset = User.active.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
