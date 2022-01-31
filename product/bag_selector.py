from.models import(Bags)

def get_Bags():
    return Bags.objects.all()

def get_Bag(Bag_id):
    return Bags.objects.get(pk=Bag_id)
   