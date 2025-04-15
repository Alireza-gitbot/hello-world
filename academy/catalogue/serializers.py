
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from catalogue.models import Brand, Product

"""
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()

    def create(self, validated_data):
        instance = Product.objects.create(**validated_data)
        return instance
"""


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ("name", "parent",)

    def validate(self, attrs):
        if len(attrs['name']) > 20:
            raise ValidationError("Caption cannot be more then 20 characters")
        return attrs

    def validate_parent(self, attr):
        return attr

    def validate(self, attrs):
        attrs['created_time'] = timezone.now()
        return attrs

    def create(self, validator_data):
        instance = super().create(validator_data)
        return instance


class ProductSerializer(serializers.ModelSerializer):
    pass