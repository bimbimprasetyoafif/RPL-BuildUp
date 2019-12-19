from django.urls import path
from products.views import ListCreateAllProduct,ListUpdateDeleteSpecificProduct, FileUploadView
from store.views import ListCreateAllStore, ListUpdateDeleteSpecificStore
from category.views import ListCreateAllCategory, ListUpdateDeleteSpecificCategory, ListCreateAllCategoryHome, ListUpdateDeleteSpecificCategoryHome

urlpatterns = [
    path('produk/',ListCreateAllProduct.as_view()),
    path('produk/gambar/upload',FileUploadView.as_view()),
    path('produk/<int:pk>', ListUpdateDeleteSpecificProduct.as_view()),

    path('toko/',ListCreateAllStore.as_view()),
    path('toko/<int:pk>', ListUpdateDeleteSpecificStore.as_view()),

    path('kategori/',ListCreateAllCategory.as_view()),
    path('kategori/<int:pk>', ListUpdateDeleteSpecificCategory.as_view()),

    path('kategorirumah/',ListCreateAllCategoryHome.as_view()),
    path('kategorirumah/<int:pk>', ListUpdateDeleteSpecificCategoryHome.as_view()),
]