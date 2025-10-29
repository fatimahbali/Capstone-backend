from django.urls import path
from .views import Home, ProjectIndex, ProjectDetail, ProjectCreate

urlpatterns = [
      path('', Home.as_view(), name='home'),
      path('projects/', ProjectIndex.as_view(), name='project-index'),
      path('projects/<int:project_id>/', ProjectDetail.as_view(), name="project-detail"),
      path('projects/create/', ProjectCreate.as_view(), name="project-create"),
      # path('projects/', ProjectCreate.as_view(), name="projects"),



]