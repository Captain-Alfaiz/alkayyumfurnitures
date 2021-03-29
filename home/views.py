from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'index.html')

def sendemail(request):
    if request.method == "POST":
        name = request.POST['name']
        message = request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = request.POST['email']
        recipient_list = [recipient_list, ]
        send_mail(name, message, email_from, recipient_list)
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')