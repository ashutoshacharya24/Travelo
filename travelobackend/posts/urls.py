from django.urls import path
from rest_framework import views
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post-list')
]
