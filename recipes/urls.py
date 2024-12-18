# recipes/urls.py

from django.urls import path 
from .views import (
    RecipeListCreateView,
    RecipeDetailView,
    TagListCreateView,
    ReviewListCreateView,
    FavoriteListCreateView,
    CommentListCreateView,
    SignupView,
)

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('favorites/', FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('signup/', SignupView.as_view(), name='signup'),
]