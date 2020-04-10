from django.shortcuts import render
from .models import Project

# Create your views here.
def portafolio(request):
    projects = Project.objects.all() #Retorna todos los objetos

    return render(request, "portfolio/portafolio.html", {'projects':projects})