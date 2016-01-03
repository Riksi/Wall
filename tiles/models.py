from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""class User(models.Model):
	username = models.CharField(max_length = 20)
	score = models.IntegerField(default=0)
	registration_date = models.DateTimeField(default=timezone.now)"""

class Tile(models.Model):
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	content = models.TextField()
	public = models.BooleanField(default = False)
	solved = models.BooleanField(default = False)
	created_date = models.DateTimeField(default=timezone.now)


# Create your models here.
