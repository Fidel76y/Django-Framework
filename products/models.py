from django.db import models

class Item(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)
    stock_status = models.CharField(max_length=20)
    available_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
