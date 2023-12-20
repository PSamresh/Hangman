from django.db import models

class HangmanGame(models.Model):
    word = models.CharField(max_length=50)
    guessed_letters = models.CharField(max_length=50, default='')
    incorrect_guesses = models.PositiveIntegerField(default=0)
    max_incorrect_guesses = models.PositiveIntegerField(default=0)
    game_state = models.CharField(max_length=20, default='InProgress')  # InProgress, Lost, Won

