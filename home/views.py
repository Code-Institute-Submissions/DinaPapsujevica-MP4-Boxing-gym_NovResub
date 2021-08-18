import json
from django.shortcuts import render
from .subscription import *
from django.http import HttpResponseRedirect, JsonResponse
from .forms import *
from .models import *
from bag.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.conf import settings
from boxing_gym.verify_request import verify_request

# Create your views here.


@verify_request
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


@verify_request
def trial(request):
    """ A view to show trial sign up page """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = 'Thank You'
        message = f'Hi {name}, thank you for registering .'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        message = "Your request has been submitted"
        return render(request, 'home/trial.html', {'message': message})

    return render(request, 'home/trial.html')


@verify_request
def classes(request):
    """ A view to show trial sign up page """

    return render(request, 'home/classes.html')


def contact(request):
    """ A view to show contact info page """

    return render(request, 'home/contact.html')


@verify_request
def select_subscription(request):
    """ A request  to select subscription plan """
    if request.method == 'POST':
        price = request.POST['price']
        subscription_name = request.POST['name']
        product = stripe_product(name=subscription_name)
        request.session['subscription'] = dict(customer_id='request.user.id', name=subscription_name,
                                               amount=float(price), status=False, method='stripe',
                                               product_id=product)

        print("request.session['subscription']", request.session['subscription'])
        return HttpResponseRedirect('/subscribe/')

    return render(request, 'home/fitnessplans.html')


@verify_request
@login_required
def create_stripe_subsription(request):
    """ A request  to handle subscription payment form stripe """

    subscription = request.session['subscription']
    if request.method == 'POST':
        card_number = request.POST['cardnumber']
        card_expyear = request.POST['expyear']
        card_expmonth = request.POST['expmonth']
        card_cvv = request.POST['card_cvv']
        card_number = str(card_number).strip()
        print(card_number, card_expyear, card_expmonth, card_cvv)
        email = request.user.email
        token_data = generate_card_token(email, card_number, card_expmonth, card_expyear, card_cvv)
        product = subscription['product_id']
        price_id = create_stripe_price(amount=subscription['amount'], interval='month', product=product)
        sub = stripe_subscription(csid=token_data['customer_id'], price_id=price_id)

        sub_data = dict(customer_id=subscription['customer_id'], name=subscription['name'],
                        amount=subscription['amount'], status=True,
                        method='stripe', payment_id=sub['id'])
        return HttpResponseRedirect('/thanks')

    return render(request, 'home/payment.html')


@verify_request
@login_required
@user_passes_test(lambda user: user.is_superuser)
def add_product(request):
    context = {}
    user = User.objects.get(id=request.user.id)
    form = ProductForm()
    if request.method == 'POST':
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        data['image_link'] = request.FILES.get('image_link')
        data['user_id'] = request.user.id
        product = Product.objects.create(**data)
        return HttpResponseRedirect('/products')
    context['form'] = form
    return render(request, "home/add_product.html", context)


@verify_request
def view_products(request):
    products = Product.objects.all()
    has_item = len(products) == 0 and request.user.is_superuser
    print("has_item", has_item)
    return render(request, 'home/products.html', {'products': products, 'has_item': has_item})


@verify_request
@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id=int(product_id))
    return render(request, 'home/product_detail.html', {'product': product})


@verify_request
@login_required
@user_passes_test(lambda user: user.is_superuser)
def edit_product(request, product_id):
    product_data = Product.objects.get(id=int(product_id))
    if request.method == 'POST':
        category = request.POST.get('category')
        name = request.POST.get('name')
        image_link = request.FILES.get('image_link', None)
        sku = request.POST.get('sku')
        price = request.POST.get('price')
        description = request.POST.get('description')
        sizes = request.POST.get('sizes')
        data = dict(name=name, image_link=image_link, sku=sku,
                    description=description, sizes=sizes, price=float(price))
        print("data:", data)
        product_data.category = category
        product_data.name = name
        if image_link is not None:
            product_data.image_link = image_link
        product_data.description = description
        product_data.sku = sku
        product_data.sizes = sizes
        product_data.price = float(price)

        product_data.save()
        return HttpResponseRedirect('/products')
    return render(request, 'home/edit_product.html',
                  {'product': product_data})


@verify_request
@login_required
@user_passes_test(lambda user: user.is_superuser)
def delete_product(request, product_id):
    Product.objects.filter(id=int(product_id)).delete()
    return HttpResponseRedirect('/products')


@verify_request
@login_required
def view_profile(request):
    """ This function dsiplay the user profile and his/her order details """

    order = Order.objects.filter(user_id=request.user.id).all()
    if len(order) == 0:
        has_order = False
    else:
        has_order = True
    result = []
    order_dates = [o.order_date.strftime('%d, %b %Y') for o in order]
    if has_order:
        order_res = [json.loads(o.original_bag) for o in order]
        for i, bags in enumerate(order_res):
            for bag in bags:
                if bag not in result:
                    bag['order_date'] = order_dates[i]
                    result.append(bag)
    print("result", order_dates)
    return render(request, 'home/profile.html', {'orders': result})


@verify_request
def subscribe(request):
    """ lead to thank you for subscribing page"""
    return render(request, 'home/subscribe.html')
