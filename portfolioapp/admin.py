from django.contrib import admin
from .models import PortfolioModel, QuotesModel

# Register your models here.

admin.site.register(PortfolioModel)
admin.site.register(QuotesModel)