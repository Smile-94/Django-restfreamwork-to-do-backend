import copy
from django.shortcuts import render
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

User=get_user_model()

from task.models import Task
from task.serializers import TaskSerializers

# Create your views here.
@api_view(['GET'])
def function_base_task_list(request, *args, **kwargs):

    try:
        task_quryset=Task.objects.all()
        task_satus=request.GET.get('status',None)

        if task_satus:
            task_quryset=task_quryset.filter(status=task_satus)

        response=TaskSerializers(data=task_quryset,many=True)
        for task in task_quryset:
            task_obj={
                'id':task.id,
                'title': task.title,
                'description': task.description,
                'created_at': task.created_at,
                'modified_at': task.modified_at,
                'status': task.status,
                'assignee': task.assignee.id
            }
            response.append(task_obj)

        return Response(response,status=status.HTTP_200_OK)

    except Exception as ex:
        print(ex)

    return Response({'Message':'Enternal Server Erro'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def function_base_create_task(request,*args, **kwargs):

    try:
        given_title=request.data.get('title', None)
        given_description=request.data.get('description', None)
        given_assignee=request.data.get('assignee', None)

        Task.objects.create(title=given_title, description=given_description, assignee_id=given_assignee)

        return Response({'message': 'Created'}, status=status.HTTP_201_CREATED)
    
    except Exception as ex:
        print(ex)
    return Response({'Message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # given_data_using_get_method=request.GET.get('data')

@api_view(['GET'])
def function_base_details_task( request, task_id, *args, **kwargs):

    try:
        task_obj=Task.objects.get(id=task_id)
        task_obj = {
            'id': task_obj.id,
            'title': task_obj.title,
            'description': task_obj.description,
            'created_at': task_obj.created_at,
            'modified_at': task_obj.modified_at,
            'status': task_obj.status,
            'assignee': task_obj.assignee.id
        }
        return Response(task_obj, status=status.HTTP_200_OK)

    except Exception as ex:
        print(f"Error ---> {ex}")
    return Response({'Message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT','PATCH'])
def function_base_update_task(request,task_id,*args, **kwargs):

    try:
        task_obj=Task.objects.get(id=task_id)
        if request.data.get('title', None):
            task_obj.title=request.data['title']
        if request.data.get('description', None):
            task_obj.description=request.data['description']
        if request.data.get('assignee', None):
            task_obj.assignee_id=request.data['assignee']

        task_obj.save()
        
        return Response({'message':'successfully update'}, status=status.HTTP_200_OK)

    except Exception as ex:
        print(f"Error ---> {ex}")
    return Response({'Message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def function_base_delete_task(request,task_id,*args, **kwargs):

    try:
        task_obj=Task.objects.filter(id=task_id).update(status='delete')
        return Response({'message':'successfully delete'}, status=status.HTTP_200_OK)

    except Exception as ex:
            print(f"Error ---> {ex}")
            
    return Response({'Message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','POST'])
def function_based_list_create_task(request,*args, **kwargs):
    try:
        if request.method=='GET':
            task_quryset=Task.objects.all()
            task_satus=request.GET.get('status',None)

            if task_satus:
                task_quryset=task_quryset.filter(status=task_satus)

            response=[]
            for task in task_quryset:
                task_obj={
                    'id':task.id,
                    'title': task.title,
                    'description': task.description,
                    'created_at': task.created_at,
                    'modified_at': task.modified_at,
                    'status': task.status,
                    'assignee': task.assignee.id
                }
                response.append(task_obj)

            return Response(response,status=status.HTTP_200_OK)
        else:
            given_title=request.data.get('title', None)
            given_description=request.data.get('description', None)
            given_assignee=request.data.get('assignee', None)

            Task.objects.create(title=given_title, description=given_description, assignee_id=given_assignee)

            return Response({'message': 'Created'}, status=status.HTTP_201_CREATED)
    
    except Exception as ex:
            print(f"Error ---> {ex}")
            
    return Response({'Message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','PUT','PATCH','DELETE'])
def function_based_detail_update_delete(request,task_id,*args, **kwargs):
    try:
        if request.method=='GET':
            task_obj=Task.objects.get(id=task_id)
            task_obj = {
                'id': task_obj.id,
                'title': task_obj.title,
                'description': task_obj.description,
                'created_at': task_obj.created_at,
                'modified_at': task_obj.modified_at,
                'status': task_obj.status,
                'assignee': task_obj.assignee.id
            }
            return Response(task_obj, status=status.HTTP_200_OK)

            return Response(response,status=status.HTTP_200_OK)

        elif request.method=='PUT' or request.method=='PATCH':
            task_obj=Task.objects.get(id=task_id)
            if request.data.get('title', None):
                task_obj.title=request.data['title']
            if request.data.get('description', None):
                task_obj.description=request.data['description']
            if request.data.get('assignee', None):
                task_obj.assignee_id=request.data['assignee']

            task_obj.save()
        
            return Response({'message':'successfully update'}, status=status.HTTP_200_OK)
        
        else:
            task_obj=Task.objects.filter(id=task_id).update(status='delete')
            return Response({'message':'successfully delete'}, status=status.HTTP_200_OK)

    
    except Exception as ex:
            print(f"Error ---> {ex}")
            
    return Response({'Message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','POST'])
def function_based_list_create_task_serilizer(request,*args, **kwargs):
    try:
        if request.method=='GET':
            task_quryset=Task.objects.all()
            task_satus=request.GET.get('status',None)

            if task_satus:
                task_quryset=task_quryset.filter(status=task_satus)

            response=TaskSerializers(instance=task_quryset,many=True)
            
            return Response(response.data,status=status.HTTP_200_OK)
        else:
            serializer=TaskSerializers(data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
    except Exception as ex:
            print(f"Error ---> {ex}")
            
    return Response({'Message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','PUT','PATCH'])
def function_based_list_details_update_task_serilizer(request,task_id,*args, **kwargs):
    try:
        task_obj=Task.objects.filter(id=task_id).first()

        if request.method=='GET':
            
            response=TaskSerializers(instance=task_obj)
            
            return Response(response.data,status=status.HTTP_200_OK)

        elif request.method=='POST' or request.method=='PATCH':

            copy_request=copy.deepcopy(request.data)
            if request.data.get('assignee', None):
                copy_request['assignee']=User.objects.filter(id=request.data['assignee']).first()

            serializer=TaskSerializers(instance=task_obj,data=request.data)
            if serializer.is_valid():
                
                serializer.update(instance=task_obj,validated_data=copy_request)

                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
    except Exception as ex:
            print(f"Error ---> {ex}")
            
    return Response({'Message': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    


    



    
