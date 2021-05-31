from django.urls import path
from .views import GetTokenView, SignupView

urlpatterns = [
    path('get_token/', GetTokenView.as_view(), name='get_token'),
    path('signup/', SignupView.as_view(), name='signup'),
    
]