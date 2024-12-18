from django.db import models
from django.contrib.auth.models import User

"""
Holds classes that define the structure of 
application data. These objects are converted
to entities using Django's ORM mapper. Also
provides mechanism for performing CRUD operations.

A Model is the single, definitive source of information
about your data. It contains the essential fields and
behaviours of the data you're storing. Generally, each
model maps to a single database table

Each model is represented by a Python class,
which is a subclass of `django.db.models.Model` class

Each model attribute represents a single database field

"""

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='recipes')
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
"""
Common Django Model Fields

1. CharField
    `name = models.CharField(max_length=100)`
    Example: `first_name = models.CharField(max_length=50, blank=True)`

2. TextField
    `description = models.TextField()`
    Example: `bio = models.TextField(blank=True)`

3. IntegerField
    `age = models.IntegerField()`
    Example: `quantity = models.IntegerField(default=0, null=True)`

4. DecimalField
    `price = models.DecimalField(max_digits=6, decimal_places=2)`
    Example: `weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True)`

5. FloatField
    `rating = models.FloatField()`
    Example: `temperature = models.FloatField(null=True)`

6. BooleanField
    `is_active = models.BooleanField(default=True)`
    Example: `completed = models.BooleanField(default=False)`

7. DateField
    `publish_date = models.DateField(auto_now_add=True)`
    Example: `birthdate = models.DateField(null=True, blank=True)`

8. DateTimeField
    `last_login = models.DateTimeField(auto_now=True)`
    Example: `event_date = models.DateTimeField(auto_now_add=True)`

9. EmailField
    `email = models.EmailField()`
    Example: `contact_email = models.EmailField(blank=True)`

10. FileField
     `resume = models.FileField(upload_to='uploads/')`
     Example: `document = models.FileField(upload_to='docs/', null=True)`
    
"""

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"
    
class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title} ({self.rating}/5)"
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"