from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cars(models.Model):
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __init__(self, model='Honda', brand='Oddysey', year='2001'):
        self.model = model
        self.brand = brand
        self.year = year

    def __str__(self):
        return self.model



