from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import User, Taller, Servicio, Review, ReviewFeedback
from .serializers import UserSerializer, TallerSerializer,ServicioSerializer, ReviewSerializer, ReviewFeedbackSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class TallerViewSet( viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer
    
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    
    
class ReviewFeedbackViewSet(viewsets.ModelViewSet):
    queryset = ReviewFeedback.objects.all()
    serializer_class = ReviewFeedbackSerializer
    