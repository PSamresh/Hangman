from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import HangmanGame  # Import your HangmanGame model

class HangmanAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()  # Create an instance of the REST framework's test client

    def test_new_game_endpoint(self):
        response = self.client.post('/new_game/')  # Make a POST request to create a new game
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Check if the response status is 201 (Created)
        self.assertIn('id', response.data)  # Check if the response contains the 'id' field
        game_id = response.data['id']  # Get the game ID from the response data

    def test_game_state_endpoint(self):
        game_id = 1  # Replace with an actual game ID for testing
        response = self.client.get(f'/game_state/{game_id}/')  # Make a GET request to fetch game state
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if the response status is 200 (OK)
        self.assertIn('game_state', response.data)  # Check if the response contains the 'game_state' field

    def test_make_guess_endpoint(self):
        game_id = 1  # Replace with an actual game ID for testing
        guess_data = {'guess': 'p'}  # Define the guess data
        response = self.client.post(f'/make_guess/{game_id}/', guess_data, format='json')  # Make a POST request to make a guess
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check if the response status is 200 (OK)
        self.assertIn('game_state', response.data)  # Check if the response contains the 'game_state' field

        # Add more assertions as needed
