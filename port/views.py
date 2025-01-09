from django.shortcuts import render, get_object_or_404
from .models import About,Education,Skills,Certificate,Project,ProjectImage


def index(request):
    about_data = About.objects.first()  # Fetch the first record
    education_data = Education.objects.all().order_by('-created_at')  # Fetch all education records
    skills = Skills.objects.all()  # Fetch all skill records
    certificates =Certificate.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {'about': about_data,'education': education_data,'skills': skills,'certificates': certificates,'projects': projects})


def project_details(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_images = ProjectImage.objects.filter(project=project)
    return render(request, 'project-details.html', {'project': project, 'project_images': project_images})