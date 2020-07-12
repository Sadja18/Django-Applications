from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    email = models.EmailField(max_length=128, unique = True)
