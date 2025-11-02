from rest_framework import serializers
from .models import Project, Task, Tasklog


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklog
        fields = "__all__"
