from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from .models import Project,  Task
from .serializers import ProjectSerializer, TaskSerializer, TaskLogSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to capstone project api home route!'}
    return Response(content)
  
class Projects(APIView):
  def get(self, request):
    content = {'message': 'Welcome to capstone project api home route!'}
    return Response(content)
  
class ProjectIndex(APIView):
  serializer_class = ProjectSerializer
  # post
  def get(self, request):
    try:
      queryset = Project.objects.all()
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def post(self, request, *args, **kwargs):
    try:
      serializer = ProjectSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProjectDetail(APIView):
  serializer_class = ProjectSerializer
  lookup_field = 'id'

  def get(self, request, project_id):
    try:
      queryset = Project.objects.get(id=project_id)
      serializer = ProjectSerializer(queryset)
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  
  def put(self, request, project_id):
    try:
        project = get_object_or_404(Project, id=project_id)
        serializer = self.serializer_class(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def delete(self, request, project_id):
    try:
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class ProjectCreate(APIView):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  
  def post(self, request, *args, **kwargs):
    try:
      serializer = ProjectSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class TasksIndex(APIView):
  serializer_class = TaskSerializer

  def get(self, request, project_id):
    try:
      tasks=Task.objects.filter(project_id=project_id)
      # queryset = Task.objects.filter(project_id=project_id)
      return Response(self.serializer_class(tasks, many=True).data, status=status.HTTP_200_OK)
    
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


  def post(self, request, project_id):
        project = get_object_or_404(Project, id=project_id)
        data = request.data.copy()
        data["project"] = project.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            tasks = Task.objects.filter(project_id=project_id)
            
            # tasks.save()
            return Response(
                self.serializer_class(tasks, many=True).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, project_id):
        task_id = request.data.get("task_id")
        task = get_object_or_404(Task, id=task_id, project_id=project_id)
        task.delete()
        tasks = Task.objects.filter(project_id=project_id)
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  

class TaskDetail(APIView):

  def get_object(self, project_id, task_id):
    return get_object_or_404(Task, id=task_id, project_id=project_id)
  
  def put(self, request, project_id, task_id):
      
      try:
        print(request.data)
        task = Task.objects.get(id=task_id, project_id=project_id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
      except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
  

  def delete(self, request, project_id, task_id):
    try:
       
        task = Task.objects.get(id=task_id, project_id=project_id, )
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

class TaskLogCreate(APIView):
   
   def post(self, request, project_id, task_id):
      task= get_object_or_404(Task, id=task_id, project_id=project_id)
      serializer = TaskLogSerializer(data={**request.data, "task": task.id})
      
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

      return Response(serializer.errors, status=400)