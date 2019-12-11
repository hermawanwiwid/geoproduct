from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
    path('getproduct', views.getproduct, name='getproduct'),
    path('getjson', views.ProductList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)