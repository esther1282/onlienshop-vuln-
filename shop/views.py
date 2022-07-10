from .models import Product, ProductImage, Category
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils.html import escape
from django.db import connection
from django.db.models.query import QuerySet

def index(request):
    all_products = Product.objects.all()

    user = request.user
    if request.user.is_authenticated is False:
        user.username = ' '

    query = request.GET.get("q")
    if query:
        cursor = connection.cursor()

        strSql = "SELECT id FROM shop_product where name LIKE '%"+query+"%' or content LIKE '%"+query+"%'"
        result = cursor.execute(strSql)
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        search_products = Product.objects.none()
        for data in datas:
            product = Product.objects.filter(id=data[0])
            search_products = search_products.union(product, all=True)

        # if search_products.count()==0:
        #     return render(request, 'shop/index.html', {'all_products': search_products, 'user': user, 'query': query})
        return render(request, 'shop/index.html', {'all_products': search_products, 'user':user, 'query':query })

    return render(request, 'shop/index.html', {'all_products': all_products, 'user':user})

def detail(request, product_id):
    user = request.user

    product = get_object_or_404(Product, pk=product_id)
    products_images = ProductImage.objects.filter(product=product)
    #quantity = forms.IntegerField(label=1)
    quantity = 1

    return render(request, 'shop/detail.html', {'product': product, 'product_images': products_images, 'user': user})


def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category_products = Product.objects.filter(category=category)

    user = request.user
    if request.user.is_authenticated is False:
        user.username = ' '

    return render(request, 'shop/index.html', {'category_name': category.title, 'all_products': category_products, 'user': user})
