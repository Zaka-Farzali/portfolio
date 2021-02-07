from django.db import models

# Create your models here.

class PortfolioModel(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='portfolioapp/images/')
    description = models.TextField(max_length=250)