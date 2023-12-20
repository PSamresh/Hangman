from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HangmanGame
from .serializers import HangmanGameSerializer
import random

WORDS = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]

@api_view(['POST'])
def new_game(request):
    word = random.choice(WORDS)
    max_incorrect_guesses = len(word) // 2
    game = HangmanGame(word=word, max_incorrect_guesses=max_incorrect_guesses)
    game.save()
    serializer = HangmanGameSerializer(game)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def game_state(request, id):
    try:
        game = HangmanGame.objects.get(pk=id)
    except HangmanGame.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = HangmanGameSerializer(game)
    return Response(serializer.data)

@api_view(['POST'])
def make_guess(request, id):
    try:
        game = HangmanGame.objects.get(pk=id)
    except HangmanGame.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    guess = request.data.get('guess', '').lower()
    word = game.word.lower()

    if guess not in word:
        game.incorrect_guesses += 1
        game.save()

    guessed_letters = ''.join([letter if letter in game.guessed_letters or letter.lower() == guess else '_'
                               for letter in word])

    if '_' not in guessed_letters:
        game.game_state = 'Won'
        game.save()
    elif game.incorrect_guesses >= game.max_incorrect_guesses:
        game.game_state = 'Lost'
        game.save()

    serializer = HangmanGameSerializer(game)
    return Response(serializer.data)

