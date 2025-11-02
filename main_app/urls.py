from django.urls import path
from .views import Home, ProjectIndex, ProjectDetail, ProjectCreate, TasksIndex, TaskDetail, TaskLogCreate

urlpatterns = [
      path('', Home.as_view(), name='home'),
      path('projects/', ProjectIndex.as_view(), name='project-index'),
      path('projects/<int:project_id>/', ProjectDetail.as_view(), name="project-detail"),
      path('projects/create/', ProjectCreate.as_view(), name="project-create"),
      # path('projects/', ProjectCreate.as_view(), name="projects"),
      path('projects/<int:project_id>/tasks/', TasksIndex.as_view(), name="tasks-create"),
      path('projects/<int:project_id>/tasks/<int:task_id>/', TaskDetail.as_view(), name="task-detail"),

      path('projects/<int:project_id>/tasks/<int:task_id>/logs/', TaskLogCreate.as_view(), name="task-log"),



]