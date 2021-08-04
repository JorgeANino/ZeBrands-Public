from django.db import transaction

from rest_framework import serializers


class SaveInTransactionMixin:
    def save(self):
        with transaction.atomic():
            return super().save()


class CatalogSystemSerializer(SaveInTransactionMixin, serializers.Serializer):
    id = serializers.IntegerField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
