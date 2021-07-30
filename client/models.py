from django.db import models
import random
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.conf import settings

# Create your models here.
class ClientModel(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password_at_time_of_creation = models.CharField(max_length=13)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True) 
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        r = random.randint(0,100)
        self.slug = slugify(self.name) + '_' + str(r)
        super(ClientModel, self).save(*args, **kwargs)
