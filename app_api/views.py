from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [JWTAuthentication]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #http_method_names = ['get']   this can be used if you need only get method
