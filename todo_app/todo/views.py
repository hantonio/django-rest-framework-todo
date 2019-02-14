from django.shortcuts import render
from rest_framework import viewsets
from todo_app.todo.models import Task
from todo_app.todo.serializers import TaskSerializer

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer



