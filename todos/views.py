from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import permissions

class ListTodo(generics.ListAPIView):
    permission_classes = (permissions.AllowAny)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer