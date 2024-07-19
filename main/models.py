from django.db import models

# Create your models here.


class Leed(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    date = models.DateTimeField()
    contacts = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.date}'
