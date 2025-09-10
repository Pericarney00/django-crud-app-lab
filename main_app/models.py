from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
  name = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField()
  console = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('game-detail', kwargs={'game_id': self.id})

class Play(models.Model):
  date = models.DateField('Last game-play')
  note = models.TextField()

  def __str__(self):
    return self.name