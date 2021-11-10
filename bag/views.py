from django.shortcuts import render
from products.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from boxing_gym.verify_request import verify_request
from home.views import build_image_url
# Create your views here.


@verify_request
@login_required
def view_shopping_bag(request):
    """
    View that renders the shopping bag page  which show the product that has been added to cart

    """
    cart_data = request.session['cart'] if 'cart' in request.session else []
    has_item = True if len(cart_data) > 0 else False
    request.session['has_item'] = has_item
    if not has_item:
        return render(request, 'bag/bag.html')
    return render(request, 'bag/bag.html', {'bag_items': cart_data, 'has_item': has_item})


@verify_request
@login_required
def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shoppingbag """

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(product_id))
        subtotal = round(float(price) * int(quantity), 2)
        total = subtotal
        image = build_image_url(str(product_data.image_link.url))
        shipping_price = 0
        total = '%.2f' % total
        subtotal = '%.2f' % subtotal
        cart_data = dict(name=product_data.name, sku=product_data.sku, size=product_data.sizes,
                         image_link=image, quantity=quantity, pid=product_id, price=price,
                         subtotal=subtotal, total=total, shipping_price=shipping_price)
        cart_result = [] if 'cart' not in request.session else request.session['cart']
        cart_result.append(cart_data)
        request.session['cart'] = cart_result
        grand_total = sum([float(d['total']) for d in cart_result])
        bag_total = sum([float(d['subtotal']) for d in cart_result])
        bag_total = '%.2f' % grand_total
        grand_total = '%.2f' % grand_total
        request.session['bag_total'] = bag_total
        request.session['grand_total'] = grand_total
        has_item = True if len(cart_result) > 0 else False
        request.session['has_item'] = has_item
        return HttpResponseRedirect('/bags')


@verify_request
@login_required
def delete_from_shopping_bag(request, pid):
    """Delete the item from the shopping bag"""
    cart_list = request.session['cart']
    for i in range(0, len(cart_list)):
        if str(cart_list[i]['pid']) == str(pid):
            del cart_list[i]
            break
    request.session['cart'] = cart_list
    grand_total = sum([float(d['total']) for d in cart_list])
    bag_total = sum([float(d['subtotal']) for d in cart_list])
    bag_total = '%.2f' % grand_total
    grand_total = '%.2f' % grand_total
    request.session['bag_total'] = bag_total
    request.session['grand_total'] = grand_total

    return HttpResponseRedirect('/bags')


@verify_request
@login_required
def update_bag(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('pid')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(product_id))
        subtotal = round(float(price) * int(quantity), 2)
        total = subtotal
        image = build_image_url(str(product_data.image_link.url))
        shipping_price = 0
        total = '%.2f' % total
        subtotal = '%.2f' % subtotal
        cart_data = dict(name=product_data.name, sku=product_data.sku, size=product_data.sizes, image_link=image,
                         quantity=quantity, pid=product_id, price=price,
                         subtotal=subtotal, total=total, shipping_price=shipping_price)

        cart_result = request.session['cart']
        new_result = []
        for d in cart_result:
            print("d['pid'] == product_id ", d['pid'] == product_id)
            if str(d['pid']) == str(product_id):
                d['quantity'] = quantity
                d['subtotal'] = subtotal
                d['total'] = total
            new_result.append(d)

        request.session['cart'] = new_result
        grand_total = sum([float(d['total']) for d in new_result])
        bag_total = sum([float(d['subtotal']) for d in new_result])
        bag_total = '%.2f' % grand_total
        grand_total = '%.2f' % grand_total
        request.session['bag_total'] = bag_total
        request.session['grand_total'] = grand_total
        has_item = True if len(cart_data) > 0 else False
        request.session['has_item'] = has_item
        return HttpResponseRedirect('/bags')


def merge(dict1, dict2):
    return dict1.update(dict2)
