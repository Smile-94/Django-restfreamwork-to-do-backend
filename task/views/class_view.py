from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView

from task.models import Task

from task.serializers import TaskListSerializer
from task.serializers import TaskSerializers


class TaskListApiView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

class TaskCreateApiView(CreateAPIView):
    serializer_class = TaskSerializers

class TaskRetriveApiView(RetrieveAPIView):
     queryset=Task.objects.all()
     serializer_class = TaskSerializers

class TaskUpdateApiView(UpdateAPIView):
    queryset=Task.objects.all()
    serializer_class = TaskSerializers

class TaskDeleteApiView(DestroyAPIView):
    queryset=Task.objects.all()

class TaskListCreateView(ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class = TaskListSerializer
    
     
class TaskDetailsUpdateView(RetrieveUpdateAPIView):
    queryset=Task.objects.all()
    serializer_class = TaskSerializers
    