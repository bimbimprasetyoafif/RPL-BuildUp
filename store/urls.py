from django.urls import path
from products.views import ListCreateAllProduct,ListUpdateDeleteSpecificProduct

urlpatterns = [
    path('produk/',ListCreateAllProduct.as_view()),
    path('produk/<int:pk>', ListUpdateDeleteSpecificProduct.as_view()),
]