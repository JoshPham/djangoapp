from django.urls import path
from . import views
from .views import GradeOverview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tutor_menu, name="tutor-menu"),
    path('grade/<int:grade_id>/', GradeOverview.as_view(), name="grade-menu"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)