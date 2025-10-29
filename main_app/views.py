from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from .models import Project
from .serializers import ProjectSerializer

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
  
  def get(self, request):
    try:
      queryset = Project.objects.all()
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
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
