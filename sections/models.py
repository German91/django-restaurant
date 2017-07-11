from django.db import models
from django.utils.text import slugify

from restaurants.models import Restaurant

class Section(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)
    restaurant = models.ForeignKey(Restaurant)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Section, self).save(*args, **kwargs)
