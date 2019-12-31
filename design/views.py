from .models import (
    Design, 
    RAB, 
    DesignImages,
    MaterialAtap,
    MaterialCatDalam,
    MaterialCatLuar,
    MaterialDinding,
    MaterialLantai,
    MaterialPlafon,
    )
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (
    DesignImagesSerializer, 
    DesignRABSerializer, 
    DesignSerializer, 
    MaterialCatExteriorSerializer,
    MaterialCatInteriorSerializer,
    MaterialDindingSerializer,
    MaterialLantaiSerializer,
    MaterialPlafonSerializer,
    MaterialAtapSerializer,
    )
from api.permissions import  IsOwnerOrReadOnly

from allUsers.models import Account
# Create your views here.

class ListCreateAllDesign(ListAPIView):
    serializer_class = DesignSerializer
    permission_classes = ()
    
    # def get_queryset(self):
    #     produk = Products.objects.all()
    #     filter_backends = [SearchFilter, OrderingFilter]
    #     search_fields = ['ProductName',]
    #     return produk
    queryset = Design.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['designName',]

    # from api.helper import get_all as get
    from api.helper import post_new_product_or_desain as post

class ListUpdateDeleteSpecificDesign(RetrieveUpdateDestroyAPIView):
    serializer_class = DesignSerializer
    permission_classes = ( IsOwnerOrReadOnly,)
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        produk = Design.objects.get(pk=pk)
        return produk

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete

class FileUploadDesignView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = ( IsOwnerOrReadOnly,)
    def post(self, request, *args, **kwargs):
        data = {}
        file_serializer = DesignImagesSerializer(data=request.data)
        idProd = request.data.get('designId')
        pkInProduk = Design.objects.get(DesignId=idProd)
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

# RAB

class ListCreateAllDesignRAB(ListAPIView):
    serializer_class = DesignRABSerializer
    permission_classes = ()
    
    def get_queryset(self):
        produk = RAB.objects.all()
        filter_backends = [SearchFilter, OrderingFilter]
        search_fields = ['productName',]
        return produk
    # queryset = Design.objects.all()
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ['DesignName',]

    from api.helper import get_all as get
    from api.helper import post_new_desain_rab_atau_material as post

class ListUpdateDeleteSpecificDesign(RetrieveUpdateDestroyAPIView):
    serializer_class = DesignRABSerializer
    permission_classes = ( IsOwnerOrReadOnly,)
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        produk = RAB.objects.get(pk=pk)
        return produk

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete

# ============================================================Material

class ListCreateAllDesignMaterialDinding(ListAPIView):
    serializer_class = MaterialDindingSerializer
    permission_classes = ()
    
    def get_queryset(self):
        produk = MaterialDinding.objects.all()
        # filter_backends = [SearchFilter, OrderingFilter]
        # search_fields = ['ProductName',]
        return produk
    # queryset = Design.objects.all()
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ['DesignName',]

    from api.helper import get_all as get
    from api.helper import post_new_desain_rab_atau_material as post

class ListCreateAllDesignMaterialPlafon(ListAPIView):
    serializer_class = MaterialPlafonSerializer
    permission_classes = ()
    
    def get_queryset(self):
        produk = MaterialPlafon.objects.all()
        # filter_backends = [SearchFilter, OrderingFilter]
        # search_fields = ['ProductName',]
        return produk
    # queryset = Design.objects.all()
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ['DesignName',]

    from api.helper import get_all as get
    from api.helper import post_new_desain_rab_atau_material as post

class ListCreateAllDesignMaterialAtap(ListAPIView):
    serializer_class = MaterialAtapSerializer
    permission_classes = ()
    
    def get_queryset(self):
        produk = MaterialAtap.objects.all()
        # filter_backends = [SearchFilter, OrderingFilter]
        # search_fields = ['ProductName',]
        return produk
    # queryset = Design.objects.all()
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ['DesignName',]

    from api.helper import get_all as get
    from api.helper import post_new_desain_rab_atau_material as post

class ListCreateAllDesignMaterialLantai(ListAPIView):
    serializer_class = MaterialLantaiSerializer
    permission_classes = ()
    
    def get_queryset(self):
        produk = MaterialLantai.objects.all()
        # filter_backends = [SearchFilter, OrderingFilter]
        # search_fields = ['ProductName',]
        return produk
    # queryset = Design.objects.all()
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ['DesignName',]

    from api.helper import get_all as get
    from api.helper import post_new_desain_rab_atau_material as post

class ListCreateAllDesignMaterialCatInterior(ListAPIView):
    serializer_class = MaterialCatInteriorSerializer
    permission_classes = ()
    
    def get_queryset(self):
        produk = MaterialCatDalam.objects.all()
        # filter_backends = [SearchFilter, OrderingFilter]
        # search_fields = ['ProductName',]
        return produk
    # queryset = Design.objects.all()
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ['DesignName',]

    from api.helper import get_all as get
    from api.helper import post_new_desain_rab_atau_material as post

class ListCreateAllDesignMaterialCatExterior(ListAPIView):
    serializer_class = MaterialCatExteriorSerializer
    permission_classes = ()
    
    def get_queryset(self):
        produk = MaterialCatLuar.objects.all()
        # filter_backends = [SearchFilter, OrderingFilter]
        # search_fields = ['ProductName',]
        return produk
    # queryset = Design.objects.all()
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ['DesignName',]

    from api.helper import get_all as get
    from api.helper import post_new_desain_rab_atau_material as post

# class ListUpdateDeleteSpecificDesign(RetrieveUpdateDestroyAPIView):
#     serializer_class = DesignRABSerializer
#     permission_classes = ( IsOwnerOrReadOnly,)
#     content = {
#                 'status': 'Not Found'
#             }

#     def get_queryset(self, pk):
#         produk = RAB.objects.get(pk=pk)
#         return produk

#     from api.helper import get_specific as get
#     from api.helper import put_specific as put
#     from api.helper import delete_specific as delete
