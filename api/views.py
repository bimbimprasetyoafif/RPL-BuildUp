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