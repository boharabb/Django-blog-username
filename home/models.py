from typing import Tuple
from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    isbn = models.CharField(max_length=250, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    bookdetail = models.TextField(null=True, blank=True)
    book_image = models.FileField(
        upload_to="Book Image", null=True, blank=True)
    
    def __str__(self):
        return self.name