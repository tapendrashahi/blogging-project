from rest_framework import serializers
from .models import Post, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug', 'description', 'created_by', 'created_at', 'is_active'
        ]

        read_only_fields = ['created_at', 'updated_at']


class TagSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Tag
        fields = [
            'id', 'name', 'slug', 'description', 'created_by', 'created_at', 'is_active' 
        ]
        read_only_fields = ['created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only= True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'meta_description', 'body', 'category', 'tag', 'author', 'created_at', 'updated_at', 'is_active']

        read_only_fields = ['created_at', 'updated_at']