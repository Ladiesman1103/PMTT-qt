from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class app(models.Model):
    name= models.CharField("Name ", max_length=240)
   
