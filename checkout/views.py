import stripe
import json
import random
from django.shortcuts import render, HttpResponseRedirect
from boxing_gym.verify_request import verify_request
from django.contrib.auth.decorators import login_required
from django.conf import settings
from dotenv import load_dotenv, find_dotenv
from bag.models import Order
from django.contrib import messages
from django.core.mail import send_mail
from bag.models import Order

from checkout.subscription import *

load_dotenv()

stripe.api_key = settings.STRIPE_KEY


# Create your views here.

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

        return HttpResponseRedirect('/subscribe/')

    return render(request, 'home/fitnessplans.html')


@verify_request
@login_required
def create_stripe_subsription(request):
    """ A request  to handle subscription payment form stripe """

    try:
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
            # perform email to the customer
            email = request.user.email
            subject = 'Thank You For Buying Plan'
            message = """
                Hi, 
                Thank you for buying plan: {name} 
                at cost of {amount} USD.
                We will be sending you further information very soon. 

                Thanks,
                Boxing Gym Team

            """.format(
                name=request.session['subscription']['name'],
                amount=request.session['subscription']['amount'],
            )
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)

            
            return HttpResponseRedirect('/thanks')

        return render(request, 'checkout/payment.html')
    except Exception as e:
        error = "Please enter valid card details !"
        messages.info(request, error)
        return HttpResponseRedirect('/subscribe')


@verify_request
def subscribe(request):
    """ lead to thank you for subscribing page"""
    return render(request, 'home/subscribe.html')


@verify_request
@login_required
def checkout_stripe_payment(request):
    """ A request api to handle stripe payment form stripe """
    try:
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
        return render(request, 'checkout/checkout.html', {'total': request.session['grand_total']})

    except Exception as e:
        error = "Please enter valid card details"
        messages.info(request, error)
        return HttpResponseRedirect('/checkout')


@verify_request
@login_required
def complete_shoping(request):
    return render(request, 'bag/thankyou.html')
