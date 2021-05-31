from rest_framework import viewsets, mixins
from . import serializers
from . import models


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class VariantViewSet(mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = serializers.VariantSerializer
    queryset = models.Variant.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

