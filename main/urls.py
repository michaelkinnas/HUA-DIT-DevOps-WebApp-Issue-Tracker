from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('issue/<int:issue_id>', views.issue, name='issue'),
    path('issues/<int:project_id>', views.issues, name='issues'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_issue/<int:project_id>', views.create_issue, name='create_issue'),
    path('register/', views.register, name='register'),
  
]