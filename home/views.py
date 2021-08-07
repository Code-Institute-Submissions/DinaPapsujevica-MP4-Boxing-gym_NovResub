from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def fitnessplans(request):
    """ A view to return the fitnessplans page """

    return render(request, 'home/fitnessplans.html')


def products(request):
    """ A view to show all products """

    return render(request, 'home/products.html')
