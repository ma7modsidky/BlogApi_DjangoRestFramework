from django.urls import path, re_path
from .views import index
from django.views.generic import TemplateView

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    # # re_path(r'^.*$', index, name='index'),
]

