from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer




class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    http_method_names = ['post']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Hash the password before saving the user
        password = make_password(serializer.validated_data['password'])

        user = User.objects.create(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=password  # Use the hashed password we get like that
        )

        return Response({"message": "User Successfully created."})





class UserLoginViewSet(viewsets.GenericViewSet):
    serializer_class = UserLoginSerializer

    @action(detail=False, methods=['post'])
    @permission_classes([AllowAny])
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])

        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'id': user.id,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
