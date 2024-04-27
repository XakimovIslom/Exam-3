from rest_framework import serializers

from store.models import Material, Warehouse, ProductMaterial


class ProductMaterialsSerializer(serializers.ModelSerializer):
    warehouses = serializers.StringRelatedField(source="warehouses__id", read_only=True)

    class Meta:
        model = Material
        fields = ("name", "warehouses")


class ProductMaterialSerializer(serializers.ModelSerializer):
    product_name = serializers.StringRelatedField(source="product.name", read_only=True)
    material = ProductMaterialsSerializer()

    class Meta:
        model = ProductMaterial
        fields = ("product_name", "quantity", "material",)


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'


class ProductMaterailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'