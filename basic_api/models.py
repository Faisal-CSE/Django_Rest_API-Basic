from django.db import models
from django.db.models.lookups import IsNull

# Create your models here.

class Artical(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=120)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
