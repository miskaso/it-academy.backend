from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title


class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/', blank=True, null=True)
    my_image = models.ImageField(upload_to='images/', blank=True, null=True)
