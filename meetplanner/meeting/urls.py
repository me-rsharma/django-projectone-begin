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
from django.urls import path

from meeting import views as meeting_view
from website import views as website_view

urlpatterns = [
    path('', website_view.meetings, name= 'meetings'),
    path('<int:id>', meeting_view.details, name='details'),
    path('rooms/', website_view.rooms, name='rooms'),
    path('rooms/<int:id>', meeting_view.room_detail, name='room_detail'),
    path('new/', meeting_view.new, name = 'new_meeting')
]
