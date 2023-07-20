from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.

def say_hello(request):
    features = Feature.objects.all()
    
    
    return render(request,'hello.html',{'features':features})

def counter(request):
    text = request.POST['text']
    words = len(text.split())
    return render(request,'counter.html',{'count':words})

def register(request):
    if request.method =='POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username,email,password)
                user.save()
                return redirect('login')
        
        else:
            messages.info(request,'Password Does not match')
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method =='POST':
        username= request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username = username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request,pk):
    
    return render(request,'post.html',{'pk':pk})