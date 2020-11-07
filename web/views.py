from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Project
from .forms import ContactForm
from portfolio.settings import RECEPIENT_EMAIL, DEFAULT_FROM_EMAIL

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

def project(request, prj_name: str):
    """Renders a single project page with detailed info
    and complete focus on this project."""

    # makes the project name better looking in the url 
    # Alien Invasion -> alien-invasion
    # def pretify_url():
    #     return prj_name.lower().replace(' ', '-')

    project = Project.objects.get(name=prj_name)
    context = {'project': project}
    return render(request, 'web/project.html', context)
    
def about_me(request):
    """About me page."""
    return render(request, 'web/about_me.html')

def contact(request):
    """Page containing the contact form plus a bit of info."""
    # SMTP server still not set up
    # https://learndjango.com/tutorials/django-email-contact-form

    #  Slight change, trying out new way of sending the email, doesn't work
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            # from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, DEFAULT_FROM_EMAIL, [RECEPIENT_EMAIL])
            except BadHeaderError:
                return HttpResponseRedirect('Invalid header found.')
            # Only for test purposes
            # In the future i will make my own logger
            print('Email Sent!')
            return redirect('web:success')
    return render(request, 'web/contact.html', {'form': form})

def success(request):
    return render(request, 'web/success.html')
