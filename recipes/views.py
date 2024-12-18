from django.shortcuts import render # To be used for rendering templates

from rest_framework import generics # provides generic views for common CRUD operations
from rest_framework.views import APIView # A base class for defining API views manually(not using generic views)
from rest_framework.response import Response # For sending back HTTP responses
from rest_framework import status # Contains HTTP status codes

from django.contrib.auth.models import User # handles user registration & authentication
from django.views.decorators.csrf import csrf_exempt 
from django.utils.decorators import method_decorator

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from .models import Recipe, Review, Favorite, Tag, Comment 

from .serializers import RecipeSerializer, FavoriteSerializer, CommentSerializer, ReviewSerializer, TagSerializer

"""
Holds request handler functions that receive HTTP requests
and return responses to the browser
"""

# Create your views here.
class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CsrfExemptSesssionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # Disable CSRF check
        return 
    
@method_decorator(csrf_exempt, name='dispatch')
class SignupView(APIView):
    authentication_classes = (CsrfExemptSesssionAuthentication)
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(username=username, password=password)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)