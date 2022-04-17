from.models import(Contact_us)

def get_agents():
    return Contact_us.objects.all()

def get_agent(agent_id):
    return Contact_us.objects.get(pk=agent_id)
   