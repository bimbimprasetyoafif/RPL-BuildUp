from .models import Cart
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CartSerializer
from api.permissions import IsAuthenticated, IsOwnerOrReadOnly

from allUsers.models import Account
# Create your views here.

class ListCreateAllCart(ListAPIView):
    serializer_class = CartSerializer
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        cartnya = Cart.objects.all()
        return cartnya

    from api.helper import get_all as get
    from api.helper import post_new_product_or_desain as post

class ListUpdateDeleteSpecificProduct(RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        cartnya = Cart.objects.get(pk=pk)
        return cartnya

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete