from django.shortcuts import render
from boxing_gym.verify_request import verify_request


# Create your views here.
@verify_request
def contact(request):
    """ A view to show contact info page """

    return render(request, 'contacts/contact.html')
