from rest_framework import viewsets, mixins
from . import serializers
from . import models
from .permissions import IsAdminOrSafe
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = [IsAdminOrSafe]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    # filtri ordine
    ordering_fields = '__all__'
    # filtri cerca
    search_fields = ['name', 'category__name',]
    # filtri url
    filterset_fields = ['category__name']


class VariantViewSet(mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = serializers.VariantSerializer
    queryset = models.Variant.objects.all()
    permission_classes = [IsAdminOrSafe]


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = [IsAdminOrSafe]

