from django.urls import path
from .views import (
    ListCreateAllProduct,
    ListUpdateDeleteSpecificProduct,
)
import uuid

urlpatterns = [
    path('produk/',ListCreateAllProduct.as_view()),
    path('produk/<uuid:pk>', ListUpdateDeleteSpecificProduct.as_view()),
]