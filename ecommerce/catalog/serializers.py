from rest_framework import serializers
from . import models


class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()
    available_sizes = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    variants = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        exclude = ['created_at']
        read_only_fields = ['created_at']

    @staticmethod
    def get_quantity(obj):
        return obj.quantity

    @staticmethod
    def get_available_sizes(obj):
        return obj.available_sizes

    @staticmethod
    def get_categories(obj):
        return CategorySerializer(models.Category.objects.filter(products=obj), many=True).data

    @staticmethod
    def get_variants(obj):
        return VariantSerializer(models.Variant.objects.filter(product=obj), many=True).data


class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Variant
        fields = '__all__'
        read_only_fields = ['product', 'sku']


class CategorySerializer(serializers.ModelSerializer):
    # products = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all(), many=True)
    # products = serializers.PrimaryKeyRelatedField(queryset=models.Product.objects.all(), many=True)
    class Meta:
        model = models.Category
        fields = '__all__'
        extra_kwargs = {'products': {'required': False}}

    def update(self, instance, validated_data):
        products = validated_data.pop('products', [])
        to_delete = []
        for p in products:
            if p in instance.products.all():
                instance.products.remove(p)
                to_delete.append(p)
        
        for p in products:
            instance.products.add(p)

        for p in to_delete:
            instance.products.remove(p)

        instance.save()
        return instance



