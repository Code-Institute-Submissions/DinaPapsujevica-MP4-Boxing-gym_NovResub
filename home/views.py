from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def fitnessplans(request):
    """ A view to return the fitnessplans page """

    return render(request, 'home/fitnessplans.html')

def trial(request):
    """ A view to show trial sign up page """

    return render(request, 'home/trial.html')
