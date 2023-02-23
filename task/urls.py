
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from task.views.function_view import function_base_task_list
from task.views.function_view import function_base_details_task
from task.views.function_view import function_base_create_task
from task.views.function_view import function_base_update_task
from task.views.function_view import function_base_delete_task
from task.views.function_view import function_based_list_create_task
from task.views.function_view import function_based_list_create_task_serilizer
from task.views.function_view import function_based_list_details_update_task_serilizer
from task.views.function_view import function_based_detail_update_delete

#class base view
from task.views.class_view import TaskListApiView
from task.views.class_view import TaskCreateApiView
from task.views.class_view import TaskRetriveApiView
from task.views.class_view import TaskUpdateApiView
from task.views.class_view import TaskDeleteApiView
from task.views.class_view import TaskListCreateView
from task.views.class_view import TaskDetailsUpdateView

from task.views.view_set import TaskViewSet

app_name='task_app'

router=router = DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('function-task-list/',function_base_task_list,name='task_list'),
    path('function-task-create/',function_base_create_task,name='task_list_create'),
    path('function-task-details/<int:task_id>/',function_base_details_task,name='task_list_detail'),
    path('function-task-update/<int:task_id>/',function_base_update_task,name='task_list_update'),
    path('function-task-delete/<int:task_id>/',function_base_delete_task,name='task_list_delete'),
    path('function-task-list-create/',function_based_list_create_task,name='task_list_list_create'),
    path('function-task-list-create-serilizer/',function_based_list_create_task_serilizer,name='task_list_list_create_serilizer'),
    path('function-task-details-update-serilizer/<int:task_id>/',function_based_list_details_update_task_serilizer,name='task_list_list_create_serilizer'),
    path('function-task-details-update-delete/<int:task_id>/',function_based_detail_update_delete,name='task_details_update_delete'),
    
]

urlpatterns += [
    path('task-list-api-view/',TaskListApiView.as_view(),name='task_list_api_view'),
    path('task-create-api-view/',TaskCreateApiView.as_view(),name='task_create_api_view'),
    path('task-detail-api-view/<int:pk>/',TaskRetriveApiView.as_view(),name='task_detail_api_view'),
    path('task-update-api-view/<int:pk>/',TaskUpdateApiView.as_view(),name='task_update_api_view'),
    path('task-delete-api-view/<int:pk>/',TaskDeleteApiView.as_view(),name='task_delete_api_view'),
    path('task-list-create-api-view/',TaskListCreateView.as_view(),name='task_list_create_api_view'),
    path('task-detail-update-api-view/<int:pk>/',TaskDetailsUpdateView.as_view(),name='task_list_create_api_view'),

]