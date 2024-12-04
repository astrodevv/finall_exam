from django.contrib import admin
from .models import Cart, Category, Product

models = [Cart, Product, Category]

for i in models:
    admin.site.register(i)
    