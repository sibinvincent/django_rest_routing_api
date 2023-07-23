from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='books')
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

