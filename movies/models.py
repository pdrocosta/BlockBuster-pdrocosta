from django.db import models
from user.models import User
from django.conf import settings
from django.db import models


class MovieRatings(models.TextChoices):
    G =  'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    NC_17 = 'NC-17'
     
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True, default=None)
    rating = models.CharField(max_length=20, choices=MovieRatings.choices, default='G', null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True, default=None)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movies")

class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    buyed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    buyed_at = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

