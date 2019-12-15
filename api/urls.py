from django.urls import path
from products.views import ListCreateAllProduct,ListUpdateDeleteSpecificProduct
from store.views import ListCreateAllStore, ListUpdateDeleteSpecificStore
from category.views import ListCreateAllCategory, ListUpdateDeleteSpecificCategory

urlpatterns = [
    path('produk/',ListCreateAllProduct.as_view()),
    path('produk/<int:pk>', ListUpdateDeleteSpecificProduct.as_view()),

    path('toko/',ListCreateAllStore.as_view()),
    path('toko/<int:pk>', ListUpdateDeleteSpecificStore.as_view()),

    path('kategori/',ListCreateAllCategory.as_view()),
    path('kategori/<int:pk>', ListUpdateDeleteSpecificCategory.as_view()),
]