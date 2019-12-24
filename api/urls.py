from django.urls import path, include
from allUsers.views import(
	registration_view,
    registration_store_view,
    registration_vendor_view,
	ObtainAuthTokenView,
	account_properties_view,
    account_properties_all_view,
	update_account_view,
	does_account_exist_view,
	ChangePasswordView,
)
from rest_framework.authtoken.views import obtain_auth_token
from products.views import ListCreateAllProduct,ListUpdateDeleteSpecificProduct, FileUploadView

from category.views import ListCreateAllCategory, ListUpdateDeleteSpecificCategory, ListCreateAllCategoryHome, ListUpdateDeleteSpecificCategoryHome
# from .views import CustomLoginView, RegisterView

urlpatterns = [
    # path('auth/login/', CustomLoginView.as_view()),
    # path('auth/registration/', RegisterView.as_view()),
    # path('auth/', include('rest_auth.urls')),

    path('profile/check/', does_account_exist_view),
	path('profile/change_password/', ChangePasswordView.as_view(), name="change_password"),
	path('profile/me/', account_properties_view, name="properties"),
	path('profile/update/', update_account_view, name="update"),
 	path('profile/login/', ObtainAuthTokenView.as_view(), name="login"), 
    # path('login', login), 

    path('toko/', account_properties_all_view.as_view()),
    # path('toko/<int:pk>',),

	path('register/', registration_view, name="register"),
    path('vendor/register/', registration_vendor_view, name="register"),
    path('toko/register/', registration_store_view, name="register"),

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