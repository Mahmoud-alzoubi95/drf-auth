from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Glass
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class PostsList(ListCreateAPIView):
    queryset = Glass.objects.all()
    serializer_class = PostSerializer

class PostsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Glass.objects.all()
    serializer_class = PostSerializer