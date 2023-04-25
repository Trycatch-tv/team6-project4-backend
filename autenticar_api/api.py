from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, authentication
from .serializers import RegisterSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required



class AutenticarViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    # queryset.save()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
