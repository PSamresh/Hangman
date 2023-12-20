from rest_framework import serializers
from .models import HangmanGame

class HangmanGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = HangmanGame
        fields = '__all__'
