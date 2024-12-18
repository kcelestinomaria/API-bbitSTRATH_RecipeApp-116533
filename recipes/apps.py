from django.apps import AppConfig

"""
Handles registration of applications
"""

class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'
