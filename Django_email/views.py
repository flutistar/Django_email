from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):

    return render(request, 'home.html')

def sendmail(request):

    send_mail(
        'Subject',
        'Email message',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

    return HttpResponse('Mail successfully sent')