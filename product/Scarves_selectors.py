from.models import(Scarves)

def get_Scarves():
    return Scarves.objects.all()

def get_scarve(scarve_id):
    return Scarves.objects.get(pk=scarve_id)
   