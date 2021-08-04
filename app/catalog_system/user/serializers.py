from rest_framework import serializers

from catalog_system.core.serializers import CatalogSystemSerializer
from user.services import create_superuser, update_superuser


class RoleSerializer(CatalogSystemSerializer):
    name = serializers.CharField()

    def validate_name(self, validated_name):
        if validated_name != "ADMIN":
            raise serializers.ValidationError(
                "Only superusers are allowed in this application"
            )
        return validated_name

    class Meta:
        fields = (
            "id",
            "name",
        )


class UserSerializer(CatalogSystemSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
        min_length=5,
    )
    roles = RoleSerializer(many=True, required=False)

    def create(self, validated_user):
        """Creates user object"""
        return create_superuser(**validated_user)

    def update(self, superuser_instance, validated_data):
        """Updates product object"""
        return update_superuser(superuser_instance=superuser_instance, **validated_data)

    class Meta:
        fields = ("id", "email", "password", "first_name", "last_name", "roles")
