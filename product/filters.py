from dataclasses import fields
from pyexpat import model
import django_filters
from .models import Bags

class Bag_filter(django_filters.FilterSet):
    item_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Bags
        fields = ['item_name']