from django.shortcuts import render
from django.http import HttpResponse


class Game:
  def __init__(self, name, genre, description, console):
    self.name = name
    self.genre = genre
    self.description = description
    self.console = console

games = [
  Game('Stardew Valley', 'farming-simulator','low-graphics, fun to play, theres no right way to play','Nintendo Switch, PC'),
  Game('Minecraft', 'survival, sandbox','low-graphics, fun to play, theres no right way to play','Nintendo Switch, PC'),
  Game('Fortnite', 'first-perspon shooter','good graphics,multi-player','Nintendo Switch'),
]

# Create your views here.


def home(request):
  return HttpResponse('<h1> howdy </h1>')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  return render(request, 'games/index.html', {'games': games})
