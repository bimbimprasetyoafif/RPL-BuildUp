from .models import Products
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer, ProductImagesSerializer
from api.permissions import IsAuthenticated, IsOwnerOrReadOnly

from allUsers.models import Account
# Create your views here.



class ListCreateAllProduct(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
       produk = Products.objects.all()
       return produk

    from api.helper import get_all as get
    from api.helper import post_new as post

class ListUpdateDeleteSpecificProduct(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        produk = Products.objects.get(pk=pk)
        return produk

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def post(self, request, *args, **kwargs):
        data = {}
        file_serializer = ProductImagesSerializer(data=request.data)
        idProd = request.data.get('ProdId')
        pkInProduk = Products.objects.get(ProductId=idProd)
        if(pkInProduk.creator == request.user):
            if file_serializer.is_valid():
                file_serializer.save()
                data["status"] = 1
                data["response"] = "succes upload"
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data["status"] = 0
            data["response"] = "UNAUTHORIZED"
            return Response(data,status=status.HTTP_401_UNAUTHORIZED)