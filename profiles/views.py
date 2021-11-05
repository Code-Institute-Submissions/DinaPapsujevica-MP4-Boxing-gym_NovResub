import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from bag.models import Order
from boxing_gym.verify_request import verify_request


# Create your views here.

@verify_request
@login_required
def view_profile(request):
    """ This function display the user profile and his/her order details """

    order = Order.objects.filter(user_id=int(request.user.id)).all()
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
    print("result", order_dates, request.user.id)
    return render(request, 'profiles/profile.html', {'orders': result})
