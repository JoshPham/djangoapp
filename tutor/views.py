from django.shortcuts import render, get_object_or_404
from django.views import View
from django.utils.text import slugify
from .models import Grade, Unit, Problem

# Create your views here.
def tutor_menu(request):
    context = {
        'grades': Grade.objects.all(),
        'units': Unit.objects.all(),
        'problems': Problem.objects.all(),
    }
    return render(request, "tutor_menu.html", context)

class GradeOverview(View):

    def get(self, request, grade_id):
        grade = get_object_or_404(Grade, grade_id=grade_id)
        units = grade.related_units.all()
        problems = Problem.objects.filter(unit__in=units)

        context = {
            'grade': grade,
            'units': units,
            'problems': problems,
        }
        return render(request, 'grade_menu.html', context)