from django.db.models import fields
from rest_framework import serializers
from . import models
from catalog import models as catalog
from catalog import serializers as catalog_serializers

class ItemSerializer(serializers.ModelSerializer):
    variant = catalog_serializers.VariantSerializerDetail()
    price = serializers.SerializerMethodField()
    class Meta:
        model = models.Item
        fields = '__all__'
        read_only_fields = ['cart']
        depth = 1

    def create(self, validated_data):
        instance = super().create(validated_data)
        user = self.context.get('user', None)
        instance.cart = models.Cart.objects.get(user=user)
        instance.save()
        return instance

    @staticmethod
    def get_price(obj):
        return obj.price


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Address
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        user = self.context.get('user', None)
        instance.cart = user
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Order
        fields = '__all__'
        read_only_fields = ['is_shipped', 'items']

    

class OrderSerializeAdmin(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'
