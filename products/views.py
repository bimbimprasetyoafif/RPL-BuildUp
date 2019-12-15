from .models import Products
from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
# Create your views here.

class ListCreateAllProduct(ListCreateAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
       produk = Products.objects.all()
       return produk

    from api.helper import get_all as get
    from api.helper import post_new as post

class ListUpdateDeleteSpecificProduct(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
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