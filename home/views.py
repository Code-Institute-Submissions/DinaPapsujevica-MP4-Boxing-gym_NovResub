import os
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from boxing_gym.verify_request import verify_request
from django.core.files.storage import FileSystemStorage


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


def build_image_url(file_url):
    print("file_url", file_url)
    file_name = file_url.split('/')[-1]
    file_name = str(file_name)
    file_link = 'uploaded_images/' + file_name
    return file_link


def handle_uploaded_file(file_name):
    path = './static/uploaded_images/' + file_name.name
    if not os.path.exists(path):
        fs = FileSystemStorage()
        filename = fs.save(path, file_name)
    return True


def error_404(request, exception):
    return render(request, '404.html', {})
