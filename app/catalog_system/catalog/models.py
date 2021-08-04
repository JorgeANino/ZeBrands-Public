from django.db import models

import uuid

from catalog_system.core.models import BaseAbstractModel


# Create your models here.
class Product(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    brand = models.CharField(max_length=255)
