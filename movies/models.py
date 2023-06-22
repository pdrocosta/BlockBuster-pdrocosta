from django.db import models
from user.models import User
# Create your models here.
class MovieRatings(models.TextChoices):
    G =  'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    NC_17 = 'NC-17'
     
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True)
    rating = models.CharField(max_length=20, choices=MovieRatings.choices, default='G', null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
