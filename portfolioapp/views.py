from django.shortcuts import render
from django.core.mail import send_mail
import re, random
from .models import PortfolioModel, QuotesModel
# Create your views here.
from portfolio.settings import EMAIL_HOST_USER

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def home(request):
    project = PortfolioModel.objects.all()
    quote = QuotesModel.objects.get(pk=random.randint(1,400))
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message_phone = request.POST['phone']
        message = request.POST['message']
        if message_name =='':
            return render(request,'home.html',{'project': project, 'quote':quote, 'error': 'Please enter your name'})
        if not (re.search(regex,message_email)):
            return render(request,'home.html',{'project': project, 'quote':quote, 'error': 'Please enter valid email'})
        if message =='':
            return render(request,'home.html',{ 'project': project, 'quote':quote, 'error': 'Please fill the message box'})
        send_mail(
            subject = 'Message from '+message_name,
            message = message + '\n' + message_email +'\n'+ message_phone ,
            from_email = EMAIL_HOST_USER,
            recipient_list = ['zeka.farzali@gmail.com'],
        )

        return render(request,'home.html',{'project': project, 'quote':quote, 'notification': 'Dear '+ message_name})
    else:
        
        return render(request,'home.html',{'project': project, 'quote':quote})

