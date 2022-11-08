from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from cart import models
from catalog import models as models_catalog
from catalog import serializers as serializers_catalog
from cart.utils.mail import notification_task
User = get_user_model()


class CartSerializers(serializers.ModelSerializer):
    quantity = serializers.IntegerField(min_value=1, max_value=10)
    size = serializers.PrimaryKeyRelatedField(queryset=models_catalog.Size.objects, required=False, default=None)
    #А на практике как лучше? Монстр сериалзатор или несколько 
    #и в get_serializer отдавать нужный?
    def __init__(self, *args, quantity=True, **kwargs):
        if not quantity:
            self.fields.pop('quantity', None)
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        quantity = validated_data.pop('quantity')
        user = self.context['request'].user
        notification_task(user.id)
        # или 404 если больше одного результата?
        item = models.Cart.objects.filter(**validated_data, user=user).first()
        if item:
            item.quantity = quantity
            item.save()
            return item
        ret = models.Cart.objects.create(
            **validated_data, quantity=quantity, user=user)
        return ret

    def validate(self, attrs):
        if not 'size' in attrs:
            if not attrs['item'].category.no_size:
                raise ValidationError('Size field is required')
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['item'] = serializers_catalog.ProductsSerializers(
            instance.item).data
        return data

    class Meta:
        model = models.Cart
        exclude = ['id', 'user']


class UserCartSerializer(serializers.ModelSerializer):
    cart_set = CartSerializers(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'cart_set']
