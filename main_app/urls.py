from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bets/', views.bets_index, name='index'),
    path('bets/track', views.bets_track, name='bet_track'),
    path('bets/create', views.BetCreate.as_view(), name='bets_create'),
    path('bettrack/create', views.BetTrackCreate.as_view(), name='bettrack_create'),
    # accounts
    path('accounts/signup/', views.signup, name='signup')
]
