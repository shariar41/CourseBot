"""
Definition of urls for CourseBot.

shariar41@gmail.com
demo
"""

from django.urls import include, path
from django.contrib import admin
from app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('api/', include('api.urls')),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
]
