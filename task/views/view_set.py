from rest_framework import viewsets
from  rest_framework.response import Response
from  rest_framework import status

from task.models import Task
from task.serializers import TaskListSerializer
from task.serializers import TaskSerializers

class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class = TaskSerializers
    lookup_field='id'

    def list(self,request,*args, **kwargs):
        try:
            queryset=self.queryset
            if request.GET.get('status',None):
                task_quryset=task_quryset.filter(request.GET['status'])
                serializer=self.get_serializer(instance=queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'messages':'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)