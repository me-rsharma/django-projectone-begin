from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from meeting.models import Meeting, Room


# we call this view function and its purpose is to handle the request send by end user
# This function to accept the request and send the response to the end user
def welcome(request):
    meetings = Meeting.objects.all()
    rooms = Room.objects.all()
    return render(request, 'website/home.html', {"meetings": meetings, "rooms": rooms})
    # return render(request, 'website/home.html', {"message":"There are currently {0} meeting scheduled in database".format(Meeting.objects.count())})
    # return HttpResponse("Welcome to the meeting planner page !!")


def meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'website/home.html', {"meetings": meetings})


def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'website/home.html', {"rooms": rooms})


# Now we need to assign url to our function so that anybody can access the response share by this view on browser
# and to do so we need to specify that in url.py file

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("I am Rajeshwar & I love coding with Python")
