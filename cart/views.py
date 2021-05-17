from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from store.models import Shoe

from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    return  render(request,'cart/summary.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        shoe_id = int(request.POST.get('shoeId'))
        shoe_qty = int(request.POST.get('shoeQty'))
        shoe = get_object_or_404(Shoe,pk=shoe_id)
        cart.add(shoe,qty=shoe_qty)

        cartqty = cart.__len__()
        return JsonResponse({'qty': cartqty})


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        shoe_id = int(request.POST.get('shoeId'))
        shoe = get_object_or_404(Shoe, id=shoe_id)
        cart.delete(shoe)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        return JsonResponse({'qty': cartqty, 'subtotal': carttotal})
    return JsonResponse('Not Found')


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        shoe_id = int(request.POST.get('shoeId'))
        shoe_qty = int(request.POST.get('shoeQty'))
        shoe = get_object_or_404(Shoe, id=shoe_id)
        cart.update(shoe,shoe_qty)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        return JsonResponse({'qty': cartqty, 'subtotal': carttotal})

    return JsonResponse('Not Found')