from .models import Players
from rest_framework import serializers


class AverageScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Players
        fields=['Nationality','Overall']

class PlayerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=Players
        fields=['Name']              