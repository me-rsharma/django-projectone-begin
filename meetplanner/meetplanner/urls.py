"""meetplanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from website import views as website_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', website_view.welcome, name='home'),
    path('date/', website_view.date, name = 'date'),
    path('about/', website_view.about, name = 'about'),
    path('meetings/', include('meeting.urls')),
]
