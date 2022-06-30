from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product, ProductImage
from .models import Order, OrderItem
from cart.models import Cart

def index(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/index.html', {'orders': orders})

def order_cart(request):
    cart = Cart.objects.get(user=request.user)
    if cart.get_active_items.count() == 0:
        return render(request, 'cart/index.html', {'cart': cart,'error_message': "주문 가능한 상품이 없습니다"})
    order = empty_order(request)
    for item in cart.get_active_items:
        if item.product.stock - item.quantity < 0:
            return render(request, 'cart/index.html', {'cart': cart, 'error_message': item.product.name+"의 재고가 없습니다"})
    for item in cart.get_active_items:
        OrderItem.objects.create(product=item.product, order=order, quantity=item.quantity)
        item.product.stock -= item.quantity
        item.product.save()
    return redirect('order:index')


def order_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.stock-1 < 0:
        products_images = ProductImage.objects.filter(product=product)
        return render(request, 'shop/detail.html', {'product': product, 'product_images': products_images, 'error_message': product.name+"의 재고가 없습니다"})
    order = empty_order(request)
    OrderItem.objects.create(product=product, order=order, quantity=1)

    product.stock -= 1
    product.save()
    return redirect('order:index')


def order(request):
    order = empty_order(request)
    return redirect('order:index')


def empty_order(request):
    order = Order.objects.create(user=request.user, shipping=3)
    return order
