from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, ImageSerializer
from .models import Post, Image
class PostViewSet(ModelViewSet):
   queryset = Post.objects.all()
   serializer_class = PostSerializer
class ImageViewSet(ModelViewSet):
   queryset = Image.objects.all()
   serializer_class = ImageSerializer
    