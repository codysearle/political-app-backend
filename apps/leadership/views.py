from django.shortcuts import render
from rest_framework import generics
from models import *
from serializers import *
from django.contrib.auth.models import User


class UserList(generics.ListCreateAPIView):
    """List all users or create a new User"""
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
