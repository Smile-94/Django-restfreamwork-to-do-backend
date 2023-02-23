from rest_framework import serializers
from task.models import Task,TaskRating
from django.contrib.auth import get_user_model

User=get_user_model()



class UserNameEmal(serializers.ModelSerializer):
   class Meta:
    model=User
    fields=('id','username','email')

class TaskSerializers(serializers.ModelSerializer):
   class Meta:
    model=Task
    fields='__all__'

class TaskRatingSerializers(serializers.ModelSerializer):
   class Meta:
    model=TaskRating
    fields='__all__'

class TaskListSerializer(serializers.ModelSerializer):

    rating=TaskRatingSerializers(many=True, read_only=True)

    class Meta:
        model=Task
        fields=('id', 'title', 'description', 'assignee','rating')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['status'] = instance.status
        # user_obj=User.objects.get(id=instance.assignee)

        # data['assignee']={
        #     'id':user_obj.id,
        #     'username':user_obj.username,
        #     'email':user_obj.email
        # }
        data['assignee']=UserNameEmal(instance=instance.assignee).data
        
        return data    

        
