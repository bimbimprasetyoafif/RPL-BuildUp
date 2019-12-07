from django.urls import path
from .views import (
    ListCreateAllProduct,
)

urlpatterns = [
    path('produk/',ListCreateAllProduct.as_view()),
]