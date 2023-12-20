from django.test import TestCase
from ..models import HangmanGame  # Import your HangmanGame model

class HangmanModelTestCase(TestCase):
    def test_game_creation(self):
        # Test creating a HangmanGame object
        game = HangmanGame.objects.create(word='Test', guessed_letters='t', incorrect_guesses=1, max_incorrect_guesses=3)
        self.assertEqual(game.word, 'Test')
        self.assertEqual(game.incorrect_guesses, 1)
        # Add more assertions as needed to test model behaviors
