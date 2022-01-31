from.models import(Women_wear)

def get_women_wears():
    return Women_wear.objects.all()

def get_women_wear(women_wear_id):
    return Women_wear.objects.get(pk=women_wear_id)
   