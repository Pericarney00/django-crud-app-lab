from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import PlayForm

# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def game_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {'games': games})

def game_detail(request, game_id):
  game = Game.objects.get(id=game_id)

  play_form = PlayForm()
  return render(request, 'games/detail.html', {'game':game, 'play_form': play_form})



class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  fields = ['genre', 'description', 'console']

class GameDelete(DeleteView):
  model = Game
  success_url ='/games/'

def add_play(request, game_id):
  form =PlayForm(request.POST)
  if form.is_valid():
    new_play = form.save(commit=False)
    new_play.game_id = game_id
    new_play.save()
  return redirect('game-detail', game_id=game_id)