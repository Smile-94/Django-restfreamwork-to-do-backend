from django.contrib import admin
from task.models import Task,TaskRating

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=('title','created_at','modified_at','status','assignee')
    search_fields=('title','assignee')
    list_filter=('title','created_at','modified_at')
    raw_id_fields=('assignee',)
    list_per_page=50

    
admin.site.register(TaskRating)