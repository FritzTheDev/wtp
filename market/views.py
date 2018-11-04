from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Listing

# Create your views here.
def index(request):
  context = {}
  context["last_ten_listings"] = Listing.objects.order_by('-listing_datetime')[:10] 
  return render(request, 'market/index.html', context)