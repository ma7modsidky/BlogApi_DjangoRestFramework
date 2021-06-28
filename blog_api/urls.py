from .views import PostList, PostDetail
from django.urls import path
app_name='blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detail_update_delete'),
    path('', PostList.as_view(), name='post_list'),
]