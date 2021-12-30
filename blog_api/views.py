from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework import status
from blog.models import Post, Comment , Category
from .serializers import PostSerializer, CommentSerializer, CommentCreateSerializer , PostCreateSerializer , CategorySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated , IsAuthenticatedOrReadOnly
from rest_framework.parsers import FormParser, MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    parser_classes = [FormParser, MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__name',]
    
    def post(self, request, *args, **kwargs):
        serializer = PostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserPosts(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permissions_classes = [IsAuthenticated]
    def get_queryset(self):
        """
        This view should return a list of all Posts
        for the currently authenticated user.
        """
        user = self.request.user
        return Post.objects.filter(author=user)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.postobjects.all()
    permission_classes = [IsAuthenticated,]
    parser_classes = [FormParser, MultiPartParser]

class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated,]
