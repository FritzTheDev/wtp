from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return HttpResponse("Hello World!")
def addJohn(request):
  user = User.objects.create_user('John', 'john@harrisranch.com', 'JohnsPassword', first_name="John", last_name="Harris")
  user.save()
  return HttpResponse("Added")