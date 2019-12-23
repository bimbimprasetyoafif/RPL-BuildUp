from django.urls import path, include
from allUsers.views import(
	registration_view,
	ObtainAuthTokenView,
	account_properties_view,
	update_account_view,
	does_account_exist_view,
	ChangePasswordView,
)
from rest_framework.authtoken.views import obtain_auth_token
from products.views import ListCreateAllProduct,ListUpdateDeleteSpecificProduct, FileUploadView
from store.views import ListCreateAllStore, ListUpdateDeleteSpecificStore
from category.views import ListCreateAllCategory, ListUpdateDeleteSpecificCategory, ListCreateAllCategoryHome, ListUpdateDeleteSpecificCategoryHome
# from .views import CustomLoginView, RegisterView

urlpatterns = [
    # path('auth/login/', CustomLoginView.as_view()),
    # path('auth/registration/', RegisterView.as_view()),
    # path('auth/', include('rest_auth.urls')),

    path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
	path('change_password/', ChangePasswordView.as_view(), name="change_password"),
	path('properties', account_properties_view, name="properties"),
	path('properties/update', update_account_view, name="update"),
 	path('login', ObtainAuthTokenView.as_view(), name="login"), 
	path('register', registration_view, name="register"),

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