from django.shortcuts import render
from .models import Destination

# Create your views here.
# To extract from database
def index(request):
    dests = Destination.objects.all()
    return render(request, "index.html", {'dests': dests})
