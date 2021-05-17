from django.http.response import  JsonResponse
from  django.shortcuts import  render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  OrderForm
from cart.cart import  Cart
from decimal import  Decimal

from .models import *


@login_required
def order_add(request):
    cart = Cart(request)
    if cart.get_total_price() <= 0:
        return redirect('store:home')
    if request.method == 'POST':
        orderForm = OrderForm(request.POST)
        if orderForm.is_valid():
            order = orderForm.save(commit=False)
            order.user_id = request.user.id
            order.save()
            for item in cart:
                OrderDetails.objects.create(order=order,shoe=item['shoe'],quantity=item['qty'],price=item['price'])
            cart.clear()
        return  render(request, 'order/order_confirm.html')

    else:
        orderForm = OrderForm()
    return render(request,'order/order.html',{'form': orderForm})




def user_orders(request,user_id):
    orders = Order.objects.filter(user_id=user_id)
    return orders