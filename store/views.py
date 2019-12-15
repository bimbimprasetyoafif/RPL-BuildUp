from .models import Stores
from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StoresSerializer
# Create your views here.

class ListCreateAllStore(ListCreateAPIView):
    serializer_class = StoresSerializer
    
    def get_queryset(self):
       objek = Stores.objects.all()
       return objek

    from api.helper import get_all as get
    from api.helper import post_new as post

class ListUpdateDeleteSpecificStore(RetrieveUpdateDestroyAPIView):
    serializer_class = StoresSerializer
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        try:
            objek = Stores.objects.get(pk=pk)
        except Stores.DoesNotExist:
            return None
        return objek

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete