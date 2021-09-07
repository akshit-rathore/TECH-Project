from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.project, name='project'),
    path('', views.project_index, name='project_index'),
] 