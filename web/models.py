from portfolio.settings import MEDIA_ROOT
from django.db import models

# Create your models here.
class Project(models.Model):
    """Model to represent a project."""
    name = models.CharField(max_length=200)
    desc = models.TextField()
    # Will include images and other juicy stuff : >
    cover = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
