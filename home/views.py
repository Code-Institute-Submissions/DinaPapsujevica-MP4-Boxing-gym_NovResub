from django.shortcuts import render
from .subscription import *
from django.http import HttpResponseRedirect, JsonResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def trial(request):
    """ A view to show trial sign up page """

    return render(request, 'home/trial.html')


def classes(request):
    """ A view to show trial sign up page """

    return render(request, 'home/classes.html')


@login_required
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
        return HttpResponseRedirect('/classes')

    return render(request, 'home/payment.html')


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


@login_required
def view_products(request):
    products = Product.objects.all()
    has_item = len(products) == 0 and request.user.is_superuser
    print("has_item", has_item)
    return render(request, 'home/products.html', {'products': products, 'has_item': has_item})


@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id=int(product_id))
    return render(request, 'home/product_detail.html', {'product': product})


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


def delete_product(request, product_id):
    Product.objects.filter(id=int(product_id)).delete()
    return HttpResponseRedirect('/products')
