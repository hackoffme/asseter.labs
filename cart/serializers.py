from rest_framework import serializers
from cart import models


class CartSerializers(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=10)

    def __init__(self, *args, quantity=True, **kwargs):
        if not quantity:
            self.fields.pop('quantity', None)
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        quantity = validated_data.pop('quantity')
        # если брать пользователя из сессии, то и права проверять не надо :)
        user = self.context['request'].user
        # или 404 если больше одного результата?
        item = models.Cart.objects.filter(**validated_data, user=user).first()
        if item:
            item.quantity = quantity
            item.save()
            return item
        return models.Cart.objects.create(**validated_data, quantity=quantity, user=user)

    class Meta:
        model = models.Cart
        exclude = ['id', 'user']


class CartAllFieldsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'
