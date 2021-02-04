from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls.static import static
from django.conf import settings

postRouter = DefaultRouter()
postRouter.register('posts', views.PostViewSet)
imageRouter = DefaultRouter()
imageRouter.register('image', views.ImageViewSet)
urlpatterns = [
   path('', include(postRouter.urls)),
   path('', include(imageRouter.urls)),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)