from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.teams, name='teams'),
    path('teams/<str:team_name>/', views.team_detail, name='team_detail'),
]