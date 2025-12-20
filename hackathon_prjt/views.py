from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.user.is_authenticated:
            return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        email=request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif pass1 != pass2:
            messages.error(request, 'Passwords do not match')
        else:
            User.objects.create_user(username=username, email=email, password=pass1)
            messages.success(request, 'Account created successfully')
            return redirect('signin')
    return render(request,'sign_up.html')


def signin(request):
        if request.user.is_authenticated:
            return redirect('home')
        if request.method == 'POST':
            username = request.POST['username']
            pass1=request.POST['pass1']
            user=authenticate(username=username,password=pass1)
            if user is not None :
                login(request,user)
                messages.success(request,"your logged in ")
                return redirect("home")
            else :
                messages.error(request,'username or password is not valid , please try again ...')
        return render(request,'sign_in.html')


@login_required
def signout(request):
    logout(request)
    messages.success(request,'you logged out successfully')
    return redirect('signin')
