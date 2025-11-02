from rest_framework import serializers
from .models import Project, Task, Tasklog
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class TaskLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklog
        fields = "__all__"

        
class TaskSerializer(serializers.ModelSerializer):
    logs=TaskLogSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # Add a password field, make it write-only
    # prevents allowing 'read' capabilities (returning the password via api response)
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  
        )
      
        return user
