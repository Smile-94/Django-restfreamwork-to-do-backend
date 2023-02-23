from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class TaskRating(models.Model):
    NAME_OPT=(
        ('excellent','Excellent'),
        ('good','Good'),
        ('poor','Poor'),
    )

    name=models.CharField(max_length=50,choices=NAME_OPT,default='good')
    created_at=models.DateTimeField( auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    STATUS_OPT=(
        ('to-do','To Do'),
        ('in-progress','In Progress'),
        ('done','Done'),
        ('delete','Delete')
    )
    title=models.CharField(max_length=500)
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20,choices=STATUS_OPT,default='to-do')
    assignee=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    rating=models.ManyToManyField(TaskRating,blank=True)


    def __str__(self) :
        return self.title[:40]