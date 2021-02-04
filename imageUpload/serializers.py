from rest_framework import serializers
from .models import Post, PostImage, Image
class PostImageSerializer(serializers.ModelSerializer):
   class Meta:
      model = PostImage
      fields = ['image']
class PostSerializer(serializers.ModelSerializer):
   images = PostImageSerializer(many=True, read_only=True)
  
   class Meta:
      model = Post
      fields = ['id', 'text', 'location', 'images']
   def create(self, validated_data):
       images_data = self.context['request'].FILES
       post = Post.objects.create(**validated_data)
       for image_data in images_data.getlist('image'):
           PostImage.objects.create(post=post, image=image_data)
       return post
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']