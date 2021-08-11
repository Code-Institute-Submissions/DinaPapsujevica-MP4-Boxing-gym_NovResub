import json
import random
from django.shortcuts import render
from home.models import *
from .models import *
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from home.subscription import generate_card_token, create_payment_charge

# Create your views here.

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


@login_required
def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shoppingbag """

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(product_id))
        subtotal = round(float(price) * int(quantity), 2)
        total = subtotal
        image = str(product_data.image_link.url)
        shipping_price = '%.2f' % 3 if subtotal < 45 else 0
        total = '%.2f' % total
        subtotal = '%.2f' % subtotal
        cart_data = dict(name=product_data.name, sku=product_data.sku, size=product_data.sizes,
                         image_link=image, quantity=quantity, pid=product_id, price=price,
                         subtotal=subtotal, total=total, shipping_price=shipping_price)
        cart_result = [] if 'cart' not in request.session else request.session['cart']
        cart_result.append(cart_data)
        print("***************************")
        print(cart_result, cart_data)
        print("***************************")
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


@login_required
def update_bag(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('pid')
        price = request.POST.get('price')
        product_data = Product.objects.get(id=int(product_id))
        subtotal = round(float(price) * int(quantity), 2)
        total = subtotal + 3.00 if subtotal < 45 else subtotal
        image = str(product_data.image_link.url)
        shipping_price = '%.2f' % 3 if subtotal < 45 else 0
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

        print("***************************")
        print(cart_data)
        print("***************************")
        print(new_result)
        print("***************************")
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


@login_required
def checkout_stripe_payment(request):
    """ A request api to handle stripe payment form stripe """

    if request.method == 'POST':
        card_number = request.POST['cardnumber']
        card_expyear = request.POST['expyear']
        card_expmonth = request.POST['expmonth']
        card_cvv = request.POST['card_cvv']
        card_number = str(card_number).strip()
        print(card_number, card_expyear, card_expmonth, card_cvv)
        email = request.user.email
        order_id = str(random.randint(123452, 984793))
        token_data = generate_card_token(email, card_number, card_expmonth, card_expyear, card_cvv)
        payment_done = create_payment_charge(token_data['card_token'], request.session['grand_total'])
        if payment_done:
            order_info = dict(order_number=order_id,
                              user_id=request.user.id,
                              stripe_pid=payment_done['id'],
                              original_bag=json.dumps(request.session['cart']),
                              order_total=request.session['bag_total'],
                              grand_total=request.session['grand_total']
                              )

            Order.objects.create(**order_info)
            del request.session['cart']
            del request.session['bag_total']
            del request.session['grand_total']
            del request.session['has_item']
        return render(request, 'bag/thankyou.html')

    return render(request, 'bag/checkout.html', {'total': request.session['grand_total']})


@login_required
def complete_shoping(request):
    return render(request, 'bag/thankyou.html')


def merge(dict1, dict2):
    return dict1.update(dict2)
