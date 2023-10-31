from django.db.models import fields
from blog.models import Category, Comment, Post
from users.models import NewUser
from rest_framework import serializers
from django.conf import settings

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('user_name', 'image', 'is_staff')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= '__all__'

class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    author = AuthorSerializer()
    class Meta:
        model = Comment
        fields = ('body', 'author', 'created',)


class CommentCreateSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.postobjects.all())
    author = serializers.PrimaryKeyRelatedField(
        queryset=NewUser.objects.all())

    class Meta:
        model = Comment
        fields = ('post', 'author', 'body', 'created')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, required=False)
    updated = serializers.DateTimeField(format="%d/%m/%Y %H:%M")
    class Meta:
        model = Post
        fields = ('id', 'title', 'author','brief','body', 'status' , 'category', 'updated' , 'image' , 'comments')

class PostCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ('title','category','brief', 'body', 'status', 'image' , 'author')


         
