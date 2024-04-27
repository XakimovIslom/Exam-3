from django.contrib import admin

from store.models import Product, Material, Warehouse, ProductMaterial

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Warehouse)
admin.site.register(ProductMaterial)

