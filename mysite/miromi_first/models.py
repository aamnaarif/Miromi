from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BeautyData(models.Model):
    name = models.CharField(max_length=100)
    height = models.FloatField()
    age = models.IntegerField(default=0)
    hair_colour = models.CharField(max_length=100)
    new_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
