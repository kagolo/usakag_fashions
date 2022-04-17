from pyexpat import model
from django.db import models
from django.db.models.fields.files import ImageField
from django_countries.fields import CountryField
# Create your models here.

class Bags(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    country=CountryField(multiple=False)
    item_image=models.ImageField(upload_to='pic')
    item_price=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    SPECIAL_DEAL_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_deal=models.CharField(max_length=200,choices=SPECIAL_DEAL_TYPE_CHOICES)
    SPECIAL_OFFER_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_offer=models.CharField(max_length=200,choices=SPECIAL_OFFER_TYPE_CHOICES)
    item_sub_image1=models.ImageField(upload_to='pic')
    item_sub_image2=models.ImageField(upload_to='pic')
    item_sub_image3=models.ImageField(upload_to='pic')

class Scarves(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    item_image=models.ImageField(upload_to='pic')
    item_price=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    SPECIAL_DEAL_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_deal=models.CharField(max_length=200,choices=SPECIAL_DEAL_TYPE_CHOICES)
    SPECIAL_OFFER_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_offer=models.CharField(max_length=200,choices=SPECIAL_OFFER_TYPE_CHOICES)
    
class Men_wear(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    country=CountryField(multiple=False)
    item_image=models.ImageField(upload_to='pic')
    item_price=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    SPECIAL_DEAL_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_deal=models.CharField(max_length=200,choices=SPECIAL_DEAL_TYPE_CHOICES)
    SPECIAL_OFFER_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_offer=models.CharField(max_length=200,choices=SPECIAL_OFFER_TYPE_CHOICES)
    item_sub_image1=models.ImageField(upload_to='pic')
    item_sub_image2=models.ImageField(upload_to='pic')
    item_sub_image3=models.ImageField(upload_to='pic')

class Women_wear(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    country=CountryField(multiple=False)
    item_image=models.ImageField(upload_to='pic')
    item_price=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    SPECIAL_DEAL_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_deal=models.CharField(max_length=200,choices=SPECIAL_DEAL_TYPE_CHOICES)
    SPECIAL_OFFER_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_offer=models.CharField(max_length=200,choices=SPECIAL_OFFER_TYPE_CHOICES)
    item_sub_image1=models.ImageField(upload_to='pic')
    item_sub_image2=models.ImageField(upload_to='pic')
   

class Special(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    item_image=models.ImageField(upload_to='pic')
    item_price1=models.CharField(max_length=200,null=False)
    item_price2=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    seller_name=models.CharField(max_length=200,null=False)

class Contact_us(models.Model):
    agent_number=models.CharField(max_length=150,null=False,unique=True)
    agent_name=models.CharField(max_length=200,null=False)
    agent_position=models.CharField(max_length=200,null=False)
    agent_contact=models.CharField(max_length=200,null=True)
    agent_image=models.ImageField(upload_to='pic')



