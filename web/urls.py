""""URL patterns for web"""

from os import stat
from django.urls import path

# For image uploads
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'web'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Projects page
    path('projects/', views.projects, name='projects'),
    # About me page
    path('about-me/', views.about_me, name='about_me'),
    # Contact page
    path('contact/', views.contact, name='contact'),

    # In progress
 
    # Single project page
    path('projects/<str:prj_name>/', views.project, name='project')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    