from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def index(request):

    return render(request,'index.html')
# def category(request):
#     return render(request,'category.html')

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Flowers
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def allflowers(request):
    flower = Flowers.objects.all()
    context = {
        'flower_list': flower
    }

    return render(request,'category.html',context)

def f_details(request,f_id):
    flower=Flowers.objects.get(id=f_id)

    return render(request,'product.html',{'product':flower})

def credential(request):
    if request.method=='POST':
        username=request.POST['username']


        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exists!!!")
                return redirect('flowershopapp:credential')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists!!!")
                return redirect('flowershopapp:credential')
            else:
                user = User.objects.create_user(username=username,email=email, password=password,)
                user.save();
                print("User saved")
                return render(request,'login.html')
        else:
            messages.info(request, "Password Not Matched")
            return redirect('flowershopapp:credential')
        return redirect('/')
    return render(request, 'cred.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('flowershopapp:index')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('flowershopapp:login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')