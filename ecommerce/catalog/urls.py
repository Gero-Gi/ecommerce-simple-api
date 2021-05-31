from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'variant', views.VariantViewSet, basename='variant')
router.register(r'category', views.CategoryViewSet, basename='category')
urlpatterns = router.urls