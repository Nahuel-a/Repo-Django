from django.urls import path
from . import views

urlpatterns = [

    path("cursos/", views.curso),
    path("altas/", views.alta_curso),

]