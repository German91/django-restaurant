from django.db import models
from django.utils.text import slugify

from cuisines.models import Cuisine

class Restaurant(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    cuisine = models.OneToOneField(Cuisine)
    phone_number = models.CharField(max_length=10)
    description = models.TextField(max_length=300, blank=True, null=True)
    promotion = models.TextField(max_length=400, blank=True, null=True)
    archived = models.BooleanField(default=False)
    logo = models.FileField(blank=True, null=True, upload_to='restaurants/')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)
