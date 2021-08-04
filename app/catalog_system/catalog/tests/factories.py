import factory
import random

from catalog_system.catalog.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    sku = factory.Faker("name")
    name = factory.Faker("name")
    price = factory.LazyAttribute(lambda x: random.randrange(1, 5))
    brand = factory.Faker("name")

    class Meta:
        model = Product
