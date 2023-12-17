from django.shortcuts import render, get_object_or_404
from .models import Grade, Unit, Problem

# Create your views here.
def tutor_home(request):
    context = {
        'grades': Grade.objects.all(),
        'units': Unit.objects.all(),
        'problems': Problem.objects.all(),
    }
    return render(request, "tutor_home.html", context)