from django.shortcuts import render
from .models import PostItem

# Create your views here.

def post(request):
    context = PostItem.objects.all()
    return render(request, "posts.html", {'posts': context})