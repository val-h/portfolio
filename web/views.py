from django.shortcuts import render

from .models import Project

# Create your views here.
def index(request):
    """Displays the home page."""
    return render(request, 'web/index.html')

def projects(request):
    """Makes a query to the database and takes all the
    projects from there, passes them as context."""
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'web/projects.html', context)

def project(request):
    """Renders a single project page with detailed info
    and complete focus on this project."""
    #return render(request, 'web/project.html')
    pass

def about_me(request):
    """About me page."""
    return render(request, 'web/about_me.html')

def contact(request):
    """Page containing the contact form plus a bit of info."""
    return render(request, 'web/contact.html')