from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    cook_time = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
