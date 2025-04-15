from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.db.models import Q

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_POST
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from basket.forms import AddToBasketForm
from catalogue.models import Product, Category, Brand, ProductType, IsActiveManager, IsActiveCategoryManager
from catalogue.serializers import BrandSerializer, ProductSerializer
from catalogue.utils import check_is_active, check_is_staff

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from catalogue.models import Product
from lib.pagination import SmallPageNumberPagination, SmallLimitOffsetPagination, SmallCursorPagination
from lib.permissions import UserOk
from rest_framework import versioning


def products_list(request):

    """
    products = Product.objects.filter(is_active=True)
    products = Product.objects.exclude(is_active=False)

    category = Category.objects.first()
    category = Category.objects.last()
    category = Category.objects.get(id=1)

    products = Product.objects.filter(is_active=True, category=category)
    category = Category.objects.filter(name='Book').first()

    products = Product.objects.filter(is_active=True, category__name='Book')

    brand = Brand.objects.first()

    product_type = ProductType.objects.filter(title='Book')
    new_product = Product.objects.create(
        product_type=product_type, upc=741852, title='Test Product',
        description=' ', category=category, brand=brand
    )

"""
    context = dict()
    context['products'] = Product.objects.select_related('category').all()
    return render(request, 'catalogue/product_list.html', context=context)


def product_detail(request, pk):
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        try:
            product = Product.objects.get(upc=pk)
        except Product.DoesNotExist:
            return HttpResponse('Product does not exist')
    """
    queryset = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    if queryset.exists():
        product = queryset.first()
        form = AddToBasketForm({"product": product.id, "quantity": 1})
        return render(request, 'catalogue/product_detail.html', {"product": product, "form": form})
    raise Http404


def category_products(request, pk):
    try:
        category = Category.objects.prefetch_related('products').get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse("Category does not exist")

    products = category.products.all()
    product_id = [1, 2, 3]
    products = Product.objects.filter(id__in=product_id)
    # products = Product.objects.filter(category=category)

    context = "\n".join([f'{product.title}, {product.upc}' for product in products])
    return HttpResponse(context)


def products_search(request):
    title = request.GET.get('q')
    products = Product.objects.actives(title__icontains=title, category__name__icontains=title)
    # products = Product.objects.filter(is_active=True).filter(title__icontains=title).filter(
    #    category__name__icontains=title).filter(category__is_active=True).distinct()
    context = "\n".join([f"{product.title}, {product.upc}" for product in products])

    return HttpResponse(f"search page: \n{context}")


@login_required(login_url='/admin/login/')
@require_http_methods(request_method_list=['GET'])
@user_passes_test(check_is_active)
@user_passes_test(lambda u: u.is_staff)
@permission_required('transaction.has_score_permission')
def user_profile(request):
    return HttpResponse(f"Hello {request.user.username}")


@login_required
# @required_GET
@require_POST
@user_passes_test(lambda u: u.score > 20)
@user_passes_test(lambda u: u.age > 14)
def campaign(request):
    return HttpResponse(f"Hello {request.user.username}")


class BrandListAPI(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)      # permission_classes = (IsAuthenticated, UserOk)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    pagination_class = SmallPageNumberPagination
    # pagination_class = SmallLimitOffsetPagination
    # pagination_class = SmallCursorPagination

    # def put(self, request, *args, **kwargs):
    #    pass

    # def delete(self, request, *args, **kwargs):
    #   pass


"""
    class ProductRetrieveAPIView(RetrieveUpdateAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductListSerializer
        permission_classes = (IsAuthenticated, )

        def get_serializer_class(self):
            if self.request.method == 'GET':
                return self.serializer_class
            return ProductCreateSerializer

        def get_queryset(self):
            qs = Super().get_queryset()
            return qs.filter(user=self.request.user)
"""

"""
class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
"""


class ProductDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


"""   
    if self.action == "GET":
        if self.request.version == '1.0':
            return BrandSerializer
        else:
            return ProductSerializer
    return self.serializer_class
"""