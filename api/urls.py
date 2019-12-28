from django.urls import path, include
from allUsers.views import(
	registration_view,
    registration_store_view,
    registration_vendor_view,
	ObtainAuthTokenView,
	account_properties_view,
    toko_properties_all_view,
    toko_properties_all_view_specific,
    vendor_properties_all_view,
    vendor_properties_all_view_specific,
	update_account_view,
	does_account_exist_view,
	ChangePasswordView,
    FileAccountUploadView,
)
from rest_framework.authtoken.views import obtain_auth_token
from products.views import (
    ListCreateAllProduct,
    ListUpdateDeleteSpecificProduct, 
    FileUploadView,
)

from category.views import (
    ListCreateAllCategory, 
    ListUpdateDeleteSpecificCategory, 
    ListCreateAllCategoryHome, 
    ListUpdateDeleteSpecificCategoryHome,
)
# from .views import CustomLoginView, RegisterView

urlpatterns = [
    # path('auth/login/', CustomLoginView.as_view()),
    # path('auth/registration/', RegisterView.as_view()),
    # path('auth/', include('rest_auth.urls')),

    path('profile/check/', does_account_exist_view), #cek profile
	path('profile/change_password/', ChangePasswordView.as_view(), name="change_password"), #ganti pass
	path('profile/me/', account_properties_view, name="properties"), #lihat profile
	path('profile/update/', update_account_view, name="update"), #update profile
 	path('profile/login/', ObtainAuthTokenView.as_view(), name="login"), #login semua user

    path('toko/', toko_properties_all_view.as_view()),
    path('toko/<int:pk>/',toko_properties_all_view_specific.as_view()),
    path('vendor/', vendor_properties_all_view.as_view()),
    path('vendor/<int:pk>/',vendor_properties_all_view_specific.as_view()),

	path('register/', registration_view, name="register"),
    path('vendor/register/', registration_vendor_view, name="register"),
    path('toko/register/', registration_store_view, name="register"),
    path('toko/register/upload/', FileAccountUploadView.as_view()),

    path('produk/',ListCreateAllProduct.as_view()),
    path('produk/gambar/upload/',FileUploadView.as_view()),
    path('produk/<int:pk>/', ListUpdateDeleteSpecificProduct.as_view()),

    # path('desain/',ListCreateAllProduct.as_view()),
    # path('desain/gambar/upload',FileUploadView.as_view()),
    # path('desain/<int:pk>', ListUpdateDeleteSpecificProduct.as_view()),

    path('kategori/',ListCreateAllCategory.as_view()),
    path('kategori/<int:pk>/', ListUpdateDeleteSpecificCategory.as_view()),

    path('kategorirumah/',ListCreateAllCategoryHome.as_view()),
    path('kategorirumah/<int:pk>/', ListUpdateDeleteSpecificCategoryHome.as_view()),
]   