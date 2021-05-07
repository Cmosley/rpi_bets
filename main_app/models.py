from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

SPORTS = (
  ('MLB', 'Baseball'),
  ('NHL', 'Hockey')
)

class Profile(models.Model): 
  total_bets: models.IntegerField()
  total_wins: models.IntegerField()
  bank_roll: models.IntegerField()
  winnings: models.DecimalField('winnings', max_digits=10, decimal_places=2)
  user = models.OneToOneField(User, on_delete=models.CASCADE)



  

class ABET(models.Model):
  start = models.DateTimeField('start', auto_now=False, auto_now_add=True)
  end = models.DateTimeField('end', auto_now=False, auto_now_add=False)
  sport = models.CharField(
    max_length=3, 
    choices=SPORTS, 
    default=SPORTS[0]
  )
  team = models.CharField(max_length=50)
  betting_line = models.IntegerField()
  bet_amount = models.DecimalField(max_digits=10, decimal_places=2)

class BBET(models.Model):
  start = models.DateTimeField('start', auto_now=False, auto_now_add=True)
  end = models.DateTimeField('end', auto_now=False, auto_now_add=False)
  sport = models.CharField(
    max_length=3, 
    choices=SPORTS, 
    default=SPORTS[0]
  )
  team = models.CharField(max_length=50)
  betting_line = models.IntegerField()
  bet_amount = models.DecimalField(max_digits=10, decimal_places=2)

class CBET(models.Model):
  start = models.DateTimeField('start', auto_now=False, auto_now_add=True)
  end = models.DateTimeField('end', auto_now=False, auto_now_add=False)
  sport = models.CharField(
    max_length=3, 
    choices=SPORTS, 
    default=SPORTS[0]
  )
  team = models.CharField(max_length=50)
  betting_line = models.IntegerField()
  bet_amount = models.DecimalField(max_digits=10, decimal_places=2)

class DBET(models.Model):
  start = models.DateTimeField('start', auto_now=False, auto_now_add=True)
  end = models.DateTimeField('end', auto_now=False, auto_now_add=False)
  sport = models.CharField(
    max_length=3, 
    choices=SPORTS, 
    default=SPORTS[0]
  )
  team = models.CharField(max_length=50)
  betting_line = models.IntegerField()
  bet_amount = models.DecimalField(max_digits=10, decimal_places=2)


class BetTrack(models.Model):
  a_bet = models.ForeignKey(ABET, on_delete=models.CASCADE)
  b_bet = models.ForeignKey(BBET, on_delete=models.CASCADE)
  c_bet = models.ForeignKey(CBET, on_delete=models.CASCADE)
  d_bet = models.ForeignKey(DBET, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created= models.DateTimeField('created', auto_now=False, auto_now_add=True)


  def __str__(self):
      return self.name