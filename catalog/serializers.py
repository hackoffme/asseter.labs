from rest_framework import serializers

from catalog import models


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'
        depth = 1
