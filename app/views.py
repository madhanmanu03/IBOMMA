from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views.generic import TemplateView


def registration(request):
    umf=UserMF()
    pmf=ProfileMF()
    d={'umf':umf,'pmf':pmf}
    if request.method=='POST' and request.FILES:
        umfd=UserMF(request.POST)
        pmfd=ProfileMF(request.POST,request.FILES)
        if umfd.is_valid() and pmfd.is_valid():
            Nud=umfd.save(commit=False)
            submittedpw=umfd.cleaned_data['password']
            Nud.set_password(submittedpw)
            Nud.save()

            Npd=pmfd.save(commit=False)
            Npd.username=Nud
            Npd.save()

            send_mail(
                'Registration',
                'Ur Ibomma Registration succefully completed.....!',
                'maheshmahi8039@gmail.com',
                [Nud.email],
                fail_silently=False),
            return render(request,'Login.html')

    return render(request,'registration.html',d)

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('Home'))
            else:
                return HttpResponse('Not active User')
    return render(request,'Login.html')
