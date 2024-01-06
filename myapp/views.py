from django.shortcuts import render,redirect
from .models import Form
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


def base(request):
    return render(request,'myapp/base.html')

def home(request):
    f=Form.objects.filter(is_delete=False)
    return render(request,'myapp/home.html',{'ff':f})

def form(request):
    user=User.objects.first()
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        city=request.POST['city']
        print(firstname,lastname,username,city)
        Form.objects.create(created_by=user,created_at=datetime.datetime.now(),firstname=firstname,lastname=lastname,username=username,city=city)
        
    return render(request,'myapp/form.html')

def delete(request,pk):
    fr=Form.objects.get(reference_id=pk)
    fr.is_delete=True
    fr.save()
    return redirect("/home")

def edit(request,pk):
    fr=Form.objects.get(reference_id=pk)
    user=User.objects.first()
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        city=request.POST['city']
        print(firstname,lastname,username,city)
        Form.objects.filter(reference_id=pk).update(updated_by=user,updated_at=datetime.datetime.now(),firstname=firstname,lastname=lastname,username=username,city=city)
        
        return redirect('/home')

    
    return render(request,'myapp/edit.html',{'fr':fr})



def login_data(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("/home")
        
        else:
            logout(request)
            redirect("/")
    return render(request,'myapp/login.html')


def logout_data(request):
    logout(request)
    return redirect('/')