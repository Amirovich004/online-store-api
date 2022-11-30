from django.db import models

# Create your models here.    title = models.CharField(max_length=100)
class Items(models.Model):
    products=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    def __str__(self):
        return self.products
