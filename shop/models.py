"""Models"""
from django.db import models

class Category(models.Model):
    """Model Category
        name: string, max: 30
    """

    name = models.CharField(max_length=30)
