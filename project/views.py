from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404

# Create your views here.
def project_index(request):
    projects = Project.objects.all()
    return render(request, 'proj/index.html', {'projects':projects})


def project(request, id):
    proj = get_object_or_404(Project, pk=id)
    return render(request, 'proj/project.html', {'object': proj})