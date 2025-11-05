from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status,permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Project,  Task, Tasklog
from .serializers import ProjectSerializer, TaskSerializer, TaskLogSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
# Define the home view

# User Registration
class LoginView(APIView):

  def post(self, request):
    try:
      username = request.data.get('username')
      password = request.data.get('password')
      user = authenticate(username=username, password=password)
      if user:
        refresh = RefreshToken.for_user(user)
        content = {'refresh': str(refresh), 'access': str(refresh.access_token),'user': UserSerializer(user).data}
        return Response(content, status=status.HTTP_200_OK)
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    try:
      user = User.objects.get(username=request.user.username)
      try:
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh),'access': str(refresh.access_token),'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
      except Exception as token_error:
        return Response({"detail": "Failed to generate token.", "error": str(token_error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
      return Response({"detail": "Unexpected error occurred.", "error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
        	    'refresh': str(refresh),
        	    'access': str(refresh.access_token),
        	    'user': UserSerializer(user).data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to capstone project api home route!'}
    return Response(content)
  
class Projects(APIView):
  def get(self, request):
    content = {'message': 'Welcome to capstone project api home route!'}
    return Response(content)
  
class ProjectIndex(APIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = ProjectSerializer
  # post
  def get(self, request):
    try:
      queryset = Project.objects.filter(user=request.user)
      serializer = ProjectSerializer(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def post(self, request, *args, **kwargs):
    try:
      serializer = ProjectSerializer(data=request.data,  context={'request': request})
      if serializer.is_valid():
        serializer.save(user_id=request.user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProjectDetail(APIView):
  permission_classes = [permissions.IsAuthenticated]

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
  permission_classes = [permissions.IsAuthenticated]

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
  permission_classes = [permissions.IsAuthenticated]

  serializer_class = TaskSerializer

  def get(self, request, project_id):
    try:
      tasks=Task.objects.filter(project_id=project_id)
      # queryset = Task.objects.filter(project_id=project_id)
      return Response(self.serializer_class(tasks, many=True).data, status=status.HTTP_200_OK)
    
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


  def post(self, request, project_id):
        try:
           
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
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, project_id):
      try:
        task_id = request.data.get("task_id")
        task = get_object_or_404(Task, id=task_id, project_id=project_id)
        task.delete()
        tasks = Task.objects.filter(project_id=project_id)
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
      except Exception as err:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
  permission_classes = [permissions.IsAuthenticated]


  def get_object(self, project_id, task_id):
    return get_object_or_404(Task, id=task_id, project_id=project_id)
  
  def put(self, request, project_id, task_id):
      
      try:
        print(request.data)
        task = Task.objects.get(id=task_id, project_id=project_id)
        serializer = TaskSerializer(task, data=request.data)
        
        if serializer.is_valid():
            Tasklog.objects.create(task=task, msg=f"Modified {task.name}, Description: {task.description}, State:{task.status}",)
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
      except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
  

  def delete(self, request, project_id, task_id):
    try:
       
        task = Task.objects.get(id=task_id, project_id=project_id, )
        task_id = task.id
        print("--------> ", task_id)
        task.delete()
        return Response({"tId": task_id}, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({' Cannot delete the task because of the error:': str(err)}, status=status.HTTP_404_NOT_FOUND)

class TaskLogCreate(APIView):
  permission_classes = [permissions.IsAuthenticated]

  serializer_class=TaskSerializer
  
  def get(self, request, project_id, task_id):
      
      try:
        logs = Tasklog.objects.filter(task_id=task_id, task__project_id=project_id)
        serializer = TaskLogSerializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      
      except Exception as err:
          return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

  def post(self, request, project_id, task_id):
    try:

      task = get_object_or_404(Task, id=task_id, project_id=project_id)
      
      data = request.data.copy()
      data = {
      'task': task.id,               
      'msg': request.data.get('msg', '')  
  }
      serializer = TaskLogSerializer(data=data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except Exception as err:
          return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)
  
  
