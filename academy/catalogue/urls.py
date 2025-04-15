
from django.urls import path
from catalogue.views import products_list, product_detail, category_products, products_search, user_profile, \
    ProductDestroyAPIView
from catalogue.views import BrandListAPI

urlpatterns = [
    path('product/list/', products_list, name='product-list'),
    path('product/search/', products_search, name='product-search'),
    path('product/detail/<int:pk>/', product_detail, name='product-detail'),
    path('category/<int:pk>/products/', category_products, name='category-detail'),
    path('profile/', user_profile, name='user-profile'),

    path('product_api/', BrandListAPI.as_view(), name='product-API'),
    # path('comment/retrieve/<int:pk>/', ProductRetrieveAPIView, name='comment-retrieve'),
    path('comment/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='comment-destroy'),

]