from.models import(Men_wear)

def get_men_wears():
    return Men_wear.objects.all()

def get_men_wear(men_wear_id):
    return Men_wear.objects.get(pk=men_wear_id)
   