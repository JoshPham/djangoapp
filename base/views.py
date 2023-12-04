from django.shortcuts import render, HttpResponse
from .models import PostItem

# Create your views here.

def home(request):
    return render(request, "home.html")

def post(request):
    context = PostItem.objects.all()
    return render(request, "post.html", {'posts': context})