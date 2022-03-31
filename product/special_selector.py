from.models import(Special)

def get_specials():
    return Special.objects.all()

def get_special(special_id):
    return Special.objects.get(pk=special_id)
   