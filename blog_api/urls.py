from .views import PostList, PostDetail , CommentCreate , UserPosts , CategoryList
from django.urls import path
app_name='blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detail_update_delete'),
    path('', PostList.as_view(), name='post_list'),
    path('createComment/', CommentCreate.as_view(), name='create_comment'),
    path('user/posts/', UserPosts.as_view(), name='user_posts'),
    path('categories/', CategoryList.as_view(), name='category_list')
]
