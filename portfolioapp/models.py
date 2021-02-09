from django.db import models
import re

# Create your models here.

class PortfolioModel(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='portfolioapp/images/')
    description = models.TextField(max_length=250)

class QuotesModel(models.Model):
    quote = models.TextField()

    def add_quotes(file):
        ff=False
        quote_text = open(file, "r", encoding="utf-8")
        string = ""
        no_quotes_list=[]
        for line in quote_text:
            string += line
        no_quotes_list=re.findall('“(.+?)”', string)
        for q in no_quotes_list:
            quotes = QuotesModel(quote=q)
            quotes.save()
