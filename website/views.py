from django.shortcuts import render, redirect
from .models import StreamerInfo

# Create your views here.
def home(request):
  sajam = StreamerInfo.objects.get(name="Sajam")
  return render(request, 'home.html', {'sajam':sajam})


def teams(request):
  team_list = ["JWong", "PhiDX", "BrawlPro", "MYK", "JoeyFury", "KFM"]
  team_info = {}

  for team in team_list:
    team_info[team] = StreamerInfo.objects.filter(team=team).order_by('rank')

  return render(request, 'teams.html', {'team_info':team_info})

def team_detail(request, team_name):
    team_members = StreamerInfo.objects.filter(team=team_name).order_by('rank')

    return render(request, 'team_detail.html', {'team_name': team_name, 'team_members': team_members})