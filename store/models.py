from django.db import models

from common.models import BaseModel


class Product(BaseModel):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Material(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Warehouse(BaseModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='warehouses')
    reminder = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.material.title} - {self.reminder}"


class ProductMaterial(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.title} - {self.material.title}"
