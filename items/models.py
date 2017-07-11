from django.db import models
from django.utils.text import slugify

from categories.models import Category

class Allergen(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Allergen, self).save(*args, **kwargs)

class Item(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, blank=True, null=True)
    allergens = models.ManyToManyField(Allergen)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Item, self).save(*args, **kwargs)
        