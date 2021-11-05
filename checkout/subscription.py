import stripe
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = settings.STRIPE_KEY


def generate_card_token(email, cardnumber, expmonth, expyear, cvv):
    data = stripe.Token.create(
        card={
            "number": str(cardnumber),
            "exp_month": int(expmonth),
            "exp_year": int(expyear),
            "cvc": str(cvv),
        })
    card_token = data['id']
    customers = stripe.Customer.list()['data']
    check_customer = [cs['id'] for cs in customers if cs['email'] == email]
    if len(check_customer) > 0:
        create_customer = check_customer[0]
    else:
        create_customer = stripe.Customer.create(
            description="sos stripe customer",
            email=email,
            metadata={"card_id": data['card']['id'], "last4": data['card']['last4']},
        )
        stripe.Customer.create_source(
            create_customer['id'],
            source=card_token,
        )

    return {"card_token": card_token, 'customer_id': create_customer}


def create_payment_charge(tokenid, amount):
    payment = stripe.Charge.create(
        amount=int(float(amount)) * 100,  # convert amount to cents
        currency='usd',
        description='Example charge',
        source=tokenid,
    )

    return {'id': payment['id'], 'paid': payment['paid']}


def create_stripe_price(amount, interval, product):
    price = stripe.Price.create(
        unit_amount=int(amount) * 100,
        currency="usd",
        recurring={"interval": interval},
        product=product
    )
    return price['id']


def stripe_subscription(csid, price_id):
    subscription = stripe.Subscription.create(
        customer=csid,
        items=[
            {"price": price_id},
        ],
    )

    return subscription


def stripe_product(name):
    product = stripe.Product.create(name=name)
    return product['id']
