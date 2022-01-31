from django.shortcuts import render,redirect
from django.http import request
from django.contrib import messages
from django.contrib.auth.models import User,auth

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout


from.models import(Bags)
from .form import RegisterUserForm
from.bag_selector import(get_Bag,get_Bags)
from.men_wear_selector import(get_men_wear,get_men_wears)
from.women_wear_selector import(get_women_wear,get_women_wears)
from.Scarves_selectors import(get_Scarves,get_scarve)

# Create your views here.

def manage_products(request):
    get_bagi = get_Bags()
    get_men_all_wear = get_men_wears()
    get_women_all_wear = get_women_wears()
    get_scarve_all = get_Scarves
    
    context={
         "get_bagi":get_bagi,
         "get_men_all_wear":get_men_all_wear,
         "get_women_all_wear":get_women_all_wear,
         "get_scarve_all":get_scarve_all
    }
    return render (request,"index.html",context)

def manage_bag_detail(request,bag_id):

    bag_detail=get_Bag(bag_id)
    context={
     "bag_detail":bag_detail
    }  
    return render(request,"bag_single.html",context)

def manage_women_wear_detail(request,women_wear_id):

    women_wear_detail=get_women_wear(women_wear_id)
    context={
     "women_wear_detail":women_wear_detail
    }  
    return render(request,"women_single.html",context)

def manage_men_wear_detail(request,men_wear_id):

    men_wear_detail=get_men_wear(men_wear_id)
    context={
     "men_wear_detail":men_wear_detail
    }  
    return render(request,"men_single.html",context)

def manage_scarve_detail(request,scarve_id):

    scarve_detail=get_scarve(scarve_id)
    context={
     "scarve_detail":scarve_detail
    }  
    return render(request,"scarves_single.html",context)

def register(request):
    form = RegisterUserForm()
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Registered successfully'+user)
            return redirect("login")

    context={
           "form":form
    }
    return render(request, "register.html",context) 

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('All_items')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:
        return render (request,'login.html')   

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")         


          




