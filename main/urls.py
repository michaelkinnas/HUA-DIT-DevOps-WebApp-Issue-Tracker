from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('issue/<int:issue_id>', views.issue, name='issue'),
    path('issues/<int:project_id>', views.issues, name='issues'),
    path('create/', views.create, name='create'),
  
]