from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField()


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)