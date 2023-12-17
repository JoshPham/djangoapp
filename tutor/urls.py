from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutor_overview, name="tutor-overview")
]