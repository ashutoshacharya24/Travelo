from django.urls import path
from . import views

urlpatterns = [
    path('profile/<uuid:pk>/', views.UserProfileView.as_view(), name='user-profile'),
    path('profile/<uuid:pk>/update/', views.UserProfileUpdateView.as_view(), name='user-profile-update'),
]
