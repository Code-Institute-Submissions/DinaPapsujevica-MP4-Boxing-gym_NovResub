from django.shortcuts import render
from .subscription import *
from django.http import HttpResponseRedirect, JsonResponse
from .forms import *
from .models import *


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
        return HttpResponseRedirect('/checkout/')

    return render(request, 'home/fitnessplans.html')


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
        email = "ashutsh@gmail.com"
        token_data = generate_card_token(email, card_number, card_expmonth, card_expyear, card_cvv)
        product = subscription['product_id']
        price_id = create_stripe_price(amount=subscription['amount'], interval='month', product=product)
        sub = stripe_subscription(csid=token_data['customer_id'], price_id=price_id)

        sub_data = dict(customer_id=subscription['customer_id'], name=subscription['name'],
                        amount=subscription['amount'], status=True,
                        method='stripe', payment_id=sub['id'])
        # Subscription.objects.create(**sub_data)
        return JsonResponse({'success': True, "subscription_id": sub['id']})

    return render(request, 'home/payment.html')


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
        return JsonResponse({'success': True, "msg": 'form saved'})
    context['form'] = form
    return render(request, "home/add_product.html", context)
