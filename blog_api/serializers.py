from django.db.models import fields
from blog.models import Category, Comment, Post
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta:
        model = Comment
        fields = ('body', 'author', 'created')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'body', 'status' , 'category', 'comments')



         
