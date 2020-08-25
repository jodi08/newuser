from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class New_User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    displayname = models.CharField(max_length=100)
    url = models.URLField(null=True)
    age = models.IntegerField(null=True)
    REQUIRED_FIELD = ['age']
    
    def __str__(self):
        return self.username

