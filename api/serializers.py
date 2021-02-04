from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = (
            'user',
            'title',
            'subtitle',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)