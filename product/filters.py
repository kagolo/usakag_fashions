from cgitb import lookup
from dataclasses import fields
from pyexpat import model
import django_filters
from django_filters import CharFilter,DateFilter
from .models import Bags
from .models import Scarves
from .models import Men_wear
from .models import Women_wear

class Bag_filter(django_filters.FilterSet):
    item_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Bags
        fields = ['item_name']

class Scarves_filter(django_filters.FilterSet):
    item_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Scarves
        fields = ['item_name']

class Men_filter(django_filters.FilterSet):
    item_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Men_wear
        fields = ['item_name']

class Women_filter(django_filters.FilterSet):
    item_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Women_wear
        fields = ['item_name']