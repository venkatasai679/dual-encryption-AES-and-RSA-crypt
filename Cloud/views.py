from django.shortcuts import render, redirect
from User.models import *
from django.contrib import messages
# Create your views here.
def cloudhome(request):
    return render(request, 'cloudhome.html')

from django.core.paginator import Paginator
def allfiles(request):
   
    files = UploadFile.objects.all()
    paginator = Paginator(files, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'allfiles.html',{'data':page_obj})

from django.db.models import Q
def requests(request):
    email = request.session['email']
    requests = RequestFile.objects.filter(Q(status='Decrypted') & Q(otp=None))
    paginator = Paginator(requests, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'requests.html',{'data':page_obj})

from django.core.mail import send_mail
import random
def sendotp(request, id):
    data = RequestFile.objects.get(id=id)
    data.otp = random.randint(1111, 9999)
    data.status='Otp is sent'
    data.save()
    email_subject = 'Key Details'
    email_message = f'Hello {data.requester},\n\nWelcome To Our Website!\n\nHere are your Key details:\nEmail: {data.requester}\nKey: {data.otp}\n\nPlease keep this information safe.\n\nBest regards,\nYour Website Team'
    send_mail(email_subject, email_message, 'cse.takeoff@gmail.com', [data.requester])
    messages.success(request, 'Otp Sent Successfully!')
    return redirect('requests')


def viewusers(request):
    users = UserModel.objects.all()
    paginator = Paginator(users, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users.html',{'data':page_obj})
