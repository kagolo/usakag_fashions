"""usakag_fashions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path
from  django.conf import settings
from  django.conf.urls.static import  static
from product import views

admin.site.site_header="Usakag fashions project"
admin.site.index_title="Usakag fashions"
admin.site.site_title="Usakag fashions Ltd"


urlpatterns = [
    path('',views.manage_products,name="All_items"),
    path('bag_detail/<int:bag_id>/',views.manage_bag_detail,name='bag_detail'),
    path('women_detail/<int:women_wear_id>/',views.manage_women_wear_detail,name='women_detail'),
    path('men_detail/<int:men_wear_id>/',views.manage_men_wear_detail,name='men_detail'),
    path('scarve_detail/<int:scarve_id>/',views.manage_scarve_detail,name='scarve_detail'),
    path('special_detail/<int:special_id>/',views.manage_special_detail,name='special_detail'),

    path("Bags_only", views.manage_bags_only,name="bags_only"),
    path("Scarves_only", views.manage_scarves_only,name="scarves_only"),
    path("Men_only", views.manage_men_only,name="men_only"),
    path("Women_only", views.manage_women_only,name="women_only"),
    path("About_us", views. manage_about_us,"about_us"),
    path("Formal", views.manage_formals,"formal"),
   
    path('admin/', admin.site.urls),

    path("register", views.register, name= "register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("contact", views.manage_contact, name="contact"),
    path("kids", views.manage_kids, name="kids"),
    path("faqs", views.manage_faqs, name="faqs")
    
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)