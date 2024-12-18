from django.contrib import admin
from .models import Recipe, Favorite, Review, Comment

"""
Holds site administration configurations

The Django Admin Interface reads metadata from our models
to provide a quick, model-centric interface where trusted users
can manage content on our site

Run the following on the terminal:
1. python manage.py makemigrations - makes the migration
2. python manage.py migrate - persists the migrations to the database

Once the above steps are complete, the models & fields(including properties)
that you created in the models.py file will be propagated to
the database.

However, to be able to later run the admin, you
need to create a superuser using the following 
command: `python manage.py createsuperuser
"""

# Register your models here.
admin.site.register([Recipe, Favorite, Review, Comment])