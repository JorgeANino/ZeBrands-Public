from .models import Product
from .utils import send_updated_product_email


def create_product(**product_data):
    """Service to create a product"""
    return Product.objects.create(**product_data)


def update_product(product_instance, **product_data):
    """Service to update a product"""
    [setattr(product_instance, attr, value) for attr, value in product_data.items()]  # noqa: E501;
    product_instance.save()
    send_updated_product_email(product_instance)
    return product_instance
