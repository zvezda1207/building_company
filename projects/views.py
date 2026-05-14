from django.shortcuts import render, get_object_or_404
from .models import Project
from .models import ProjectImage

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def gallery(request):
    images = ProjectImage.objects.all().order_by('-id')
    return render(request, 'projects/gallery.html', {'images': images})
