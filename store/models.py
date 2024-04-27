from django.db import models

from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Material(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Warehouse(BaseModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='warehouses')
    reminder = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.material.name} - {self.reminder}"


class ProductMaterial(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='materials')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.material.name}"
