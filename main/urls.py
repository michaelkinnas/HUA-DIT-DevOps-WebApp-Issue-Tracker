from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('issue/<int:id>', views.issue, name='issue'),
    path('create/', views.create, name='create'),
  
]