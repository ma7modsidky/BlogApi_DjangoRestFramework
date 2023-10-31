from .views import PostList, PostDetail, CommentCreate, UserPosts, CategoryList
from django.urls import path
app_name= 'blog_api'

urlpatterns = [
    path('posts/<int:pk>/', PostDetail.as_view(), name='detail_update_delete'),
    path('posts/', PostList.as_view(), name='post_list'),

    path('posts/<int:pk>/comments/', CommentCreate.as_view(), name='create_comment'),

    # path('posts/user/', UserPosts.as_view(), name='user_posts'),
    path('categories/', CategoryList.as_view(), name='category_list')
]
