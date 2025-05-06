# UserApp/serializers.py
from rest_framework import serializers

class QuestionnaireSerializer(serializers.Serializer):
    preferences = serializers.ListField(
        child=serializers.ChoiceField(choices=['vegan', 'vegetarian', 'keto', 'gluten_free']),
        required=False
    )
    allergies = serializers.ListField(
        child=serializers.ChoiceField(choices=['nuts', 'dairy', 'seafood']),
        required=False
    )
    budget = serializers.DecimalField(max_digits=6, decimal_places=2, required=False)
    eco_friendly = serializers.BooleanField(default=False)
    
    max_calories = serializers.IntegerField(required=False)
