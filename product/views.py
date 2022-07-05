from django.shortcuts import render,redirect
from django.http import request
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required,user_passes_test

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.template import context


from.models import(Bags)
from .form import RegisterUserForm
from.bag_selector import(get_Bag,get_Bags)
from.men_wear_selector import(get_men_wear,get_men_wears)
from.women_wear_selector import(get_women_wear,get_women_wears)
from.Scarves_selectors import(get_Scarves,get_scarve)
from.special_selector import(get_special,get_specials)
from.Contact_selector import(get_agents)

from .filters import Bag_filter
from .filters import Scarves_filter
from .filters import Men_filter


# Create your views here.

def manage_products(request):
    get_bagi = get_Bags()
    get_men_all_wear = get_men_wears()
    get_women_all_wear = get_women_wears()
    get_scarve_all = get_Scarves()
    get_special_all = get_specials()
    
    context={
         "get_bagi":get_bagi,
         "get_men_all_wear":get_men_all_wear,
         "get_women_all_wear":get_women_all_wear,
         "get_scarve_all":get_scarve_all,
         "get_special_all":get_special_all,

    }
    return render (request,"index.html",context)
  
@user_passes_test(lambda u: u.is_superuser, login_url='login')
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
     "men_wear_detail":men_wear_detail,
    }  
    return render(request,"men_single.html",context)

def manage_scarve_detail(request,scarve_id):

    scarve_detail=get_scarve(scarve_id)
    context={
     "scarve_detail":scarve_detail
    }  
    return render(request,"scarves_single.html",context)


def manage_special_detail(request,special_id):

    special_detail=get_special(special_id)
    context={
        "special_detail":special_detail
    }
    return render(request,"special_single.html",context)



def register(request):
    form = RegisterUserForm()
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username','last_name')
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

def manage_bags_only(request):
    get_bagi = get_Bags()

    user_bag_filter = Bag_filter(request.GET, queryset=get_bagi)
    
    context={
        "user_bag_filter":user_bag_filter
    }
    return render(request,'bags_only.html', context)

def manage_scarves_only(request):
    get_scarve_all = get_Scarves()
    
    user_scarve_filter = Scarves_filter(request.GET, queryset=get_scarve_all)

    context={
          "user_scarve_filter":user_scarve_filter,
    }
    return render(request,'scarves_only.html',context)

def manage_men_only(request):
    get_men_all_wear = get_men_wears()

    user_men_filter = Men_filter(request.GET, queryset=get_men_all_wear)

    context={
        "user_men_filter":user_men_filter,
    }
    return render(request,'men_only.html',context)

def manage_women_only(request):
    get_women_all_wear = get_women_wears()

    user_women_filter = Men_filter(request.GET, queryset=get_women_all_wear)

    context={
        "user_women_filter":user_women_filter,
    }
    return render(request,'women_only.html',context)

     


def manage_about_us(request):
    return render(request,'about.html',context)

def manage_formals(request):
    return render(request,'formals.html')


def manage_contact(request):
    
    get_special_coll = get_specials()
    get_agents_all = get_agents()

    context={
        "get_special_coll":get_special_coll,
        "get_agents_all":get_agents_all,
    }
    return render(request, 'contact.html',context)

def manage_kids(request):
    return render(request, 'kids.html')

def manage_faqs(request):
    return render(request, 'faq.html')


# filters


          




