from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TallerViewSet, ServicioViewSet, ReviewViewSet, ReviewFeedbackViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'talleres', TallerViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'review_feedback', ReviewFeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]