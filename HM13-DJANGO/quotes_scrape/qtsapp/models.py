from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=120, null=False)
    born_date = models.CharField(max_length=120)
    born_location = models.CharField(max_length=120)
    description = models.TextField()

class Quote(models.Model):
    tags = ArrayField(models.CharField(max_length=40))
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()
