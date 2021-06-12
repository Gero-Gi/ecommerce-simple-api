from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from . import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemSerializer
    permission_classes = [permissions.ItemPermission]
    filter_backends = [DjangoFilterBackend]

    # filtri url
    filterset_fields = ['is_active']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_superuser: return models.Item.objects.all()
        user = self.request.user
        queryset = models.Item.objects.filter(cart__user=user)
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.AdminOrOwner]

    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    # filtri ordine
    ordering_fields = '__all__'
    # filtri url
    filterset_fields = ['is_shipped']

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return serializers.OrderSerializeAdmin
        return serializers.OrderSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_superuser: return models.Order.objects.all()
        user = self.request.user
        queryset = models.Order.objects.filter(user=user)
        return queryset
    

class AddressViewSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    permission_classes = [permissions.AdminOrOwner]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        if self.request.user.is_superuser: return models.Address.objects.all()
        user = self.request.user
        queryset = models.Address.objects.filter(user=user)
        return queryset

    