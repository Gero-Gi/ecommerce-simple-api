from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'order', views.OrderViewSet, basename='order')
# router.register(r'cart', views.Ca, basename='cart')
router.register(r'item', views.ItemViewSet, basename='item')
router.register(r'address', views.AddressViewSet, basename='address')

urlpatterns = router.urls