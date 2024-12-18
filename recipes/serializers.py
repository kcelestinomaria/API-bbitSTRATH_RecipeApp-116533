from rest_framework import serializers
from .models import Recipe, Favorite, Review, Comment, Tag

# Serializer for Tag Model
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ['id', 'name', 'description']

# Serializer for Recipe Model
class RecipeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'created_by', 'reviews', 'comments']

# Serializer for Favorite Model
class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'recipe']

# Serializer for Review Model
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    recipe = serializers.ReadOnlyField(source='recipe.title')

    class Meta:
        model = Review
        fields = ['id', 'recipe', 'user', 'rating', 'comment', 'created_at']

# Serializer for Comment Model
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    recipe = serializers.ReadOnlyField(source='recipe.title')

    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'user', 'text', 'created_at']