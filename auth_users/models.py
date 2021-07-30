from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #Boolean fields to select the type of account.
	is_administrator = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)
	is_client = models.BooleanField(default=False)
	is_parent = models.BooleanField(default=False)