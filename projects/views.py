from django.shortcuts import render
from .import models

# Create your views here

def projects_view(request):
    #logic to fetch and display projects can be added here in the future project
    projects_list = models.Project.objects.all().order_by('-year')
    context = {'projects_list': projects_list}

    return render(request, 'projects/projects.html', context)



