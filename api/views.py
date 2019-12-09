from .models import Product, ProductOwner
from .helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
# Create your views here.

class ListCreateAllProduct(ListCreateAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
       produk = Product.objects.all()
       return produk

    from .helper import get_all as get
    from .helper import post_new as post

class ListUpdateDeleteSpecificProduct(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        try:
            produk = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None
        return produk

    from .helper import get_specific as get
    from .helper import put_specific as put
    from .helper import delete_specific as delete