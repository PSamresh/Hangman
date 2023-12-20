# /hangman_project/hangman_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('/new_game/', views.new_game, name='new_game'),
    path('game_state/<int:id>/', views.game_state, name='game_state'),
    path('make_guess/<int:id>/', views.make_guess, name='make_guess'),
]
