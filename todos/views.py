from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import AllowAny

class ListTodo(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer