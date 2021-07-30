from django.db import models
# Create your models here.

class CatagoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('event_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)



class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    #catagory = models.ForeignKey(CatagoryModel,related_name='catagories', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250,null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }
        return reverse('event_detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)
