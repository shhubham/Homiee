from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class detail(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    thumb=models.ImageField(default='default.png',blank=True)
    author=models.ForeignKey(User,default=None)

    def __str__(self):
        return self.title
