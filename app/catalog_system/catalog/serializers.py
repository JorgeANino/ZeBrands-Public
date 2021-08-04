from rest_framework import serializers

from catalog_system.core.serializers import CatalogSystemSerializer
from .services import create_product, update_product
from .models import Product


class ProductSerializer(CatalogSystemSerializer):
    id = serializers.UUIDField(required=False)
    sku = serializers.CharField(required=True, max_length=255)
    name = serializers.CharField(required=True, max_length=255)
    price = serializers.FloatField()
    brand = serializers.CharField(required=True, max_length=255)

    def create(self, validated_menu_option):
        """Creates product object"""
        return create_product(**validated_menu_option)

    def update(self, product_instance, validated_data):
        """Updates product object"""
        return update_product(product_instance=product_instance, **validated_data)

    def validate(self, data):
        """Validates that a product with that sku doesn't exist"""
        if not data.get("sku"):
            raise serializers.ValidationError("SKU can't be null.")
        if Product.objects.filter(sku=data.get("sku"), pk=data.get("id")).exists():
            raise serializers.ValidationError("A product with that sku already exist.")
        return data

    class Meta:
        fields = ("id", "sku", "name", "price", "brand")
