from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationViewSet, UserLoginViewSet

router = DefaultRouter()
router.register(r'register',UserRegistrationViewSet , basename='registration'),
router.register(r'login', UserLoginViewSet, basename='user-login'),


urlpatterns = [
    path('',include(router.urls)),
]
