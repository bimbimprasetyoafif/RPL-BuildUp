from .models import Products
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer, ProductImagesSerializer
from api.permissions import IsAuthenticated, IsOwnerOrReadOnly
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
        try:
            produk = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            return None
        return produk

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = ProductImagesSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)