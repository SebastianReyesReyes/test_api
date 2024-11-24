from rest_framework import serializers
from .models import User, Taller, Servicio, Review, ReviewFeedback

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = '__all__'
        
class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class ReviewFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewFeedback
        fields = '__all__'
        