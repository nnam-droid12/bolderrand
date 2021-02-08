from django.shortcuts import render
#from .models import *  
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

def home(request):
    context = {}

    return render (request, 'errands/home.html', context)

def contact(request):
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')

        html_message = render_to_string(
            'errands/contact.html',
            {'name':message_name, 
            'email':message_email, 
            'message':message}
        )
        plain_message = strip_tags(html_message)
        html_message = html_message.replace("\r\n", "<br>")

        send_mail(
            'message from ' + str(message_name),
            plain_message,
            message_email,
            ['williamdev95@gmail.com', message_email],
            html_message = html_message
            )
        context = {'message_name': message_name}    
        return render(request, 'errands/contact.html', context)
    else:
        return render (request, 'errands/contact.html')

def about(request):
    context = {}
    return render (request, 'errands/about.html', context)

def services(request):
    context = {}
    return render (request, 'errands/services.html', context)    
