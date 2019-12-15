from .models import Categorys,CategorysHome
from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CategorySerializer,CategoryHomeSerializer
# Create your views here.

class ListCreateAllCategory(ListCreateAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
       objek = Categorys.objects.all()
       return objek

    from api.helper import get_all as get
    from api.helper import post_new as post

class ListUpdateDeleteSpecificCategory(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        try:
            objek = Categorys.objects.get(pk=pk)
        except Categorys.DoesNotExist:
            return None
        return objek

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete

class ListCreateAllCategoryHome(ListCreateAPIView):
    serializer_class = CategoryHomeSerializer
    
    def get_queryset(self):
       objek = CategorysHome.objects.all()
       return objek

    from api.helper import get_all as get
    from api.helper import post_new as post

class ListUpdateDeleteSpecificCategoryHome(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryHomeSerializer
    content = {
                'status': 'Not Found'
            }

    def get_queryset(self, pk):
        try:
            objek = CategorysHome.objects.get(pk=pk)
        except CategorysHome.DoesNotExist:
            return None
        return objek

    from api.helper import get_specific as get
    from api.helper import put_specific as put
    from api.helper import delete_specific as delete