from .models import Vendors
from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import VendorsSerializer
# Create your views here.

class ListCreateAllStore(ListCreateAPIView):
    serializer_class = VendorsSerializer
    
    def get_queryset(self):
       objek = Vendors.objects.all()
       return objek

    from api.helper import get_all as get
    from api.helper import post_new as post

class ListUpdateDeleteSpecificStore(RetrieveUpdateDestroyAPIView):
    serializer_class = VendorsSerializer
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        try:
            objek = Vendors.objects.get(pk=pk)
        except Vendors.DoesNotExist:
            return None
        return objek

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete