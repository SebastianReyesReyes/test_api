from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status, permissions, serializers
from .models import User, Taller, Servicio, Review, ReviewFeedback
from .serializers import UserSerializer, TallerSerializer,ServicioSerializer, ReviewSerializer, ReviewFeedbackSerializer
from .permissions import IsAdminUser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

    
class TallerViewSet( viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'An unexpected error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'An unexpected error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist as e:
            return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'An unexpected error occurred: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

    
class ServicioViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

    
class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer    
    
    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

    
class ReviewFeedbackViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = ReviewFeedback.objects.all()
    serializer_class = ReviewFeedbackSerializer

    # def get_permissions(self):
    #     if self.action in ['list', 'retrieve']:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

class ContactForm(serializers.Serializer):
      # simple serializer for emails
    email = serializers.EmailField()
    message = serializers.CharField()
# simple endpoint to take the serializer data
class SendEmail(APIView):
      # permission class set to be unauthenticated
    permission_classes = (permissions.AllowAny,)
    # this is where the drf-yasg gets invoked
    @swagger_auto_schema(request_body=ContactForm)
    def post(self, request):
          # serializer object
        serializer = ContactForm(data=request.data)
        # checking for errors
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)