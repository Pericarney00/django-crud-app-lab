from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.


def home(request):
  return HttpResponse('<h1> howdy </h1>')

def about(request):
  return render(request, 'about.html')

def game_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {'games': games})

def game_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', {'game':game})