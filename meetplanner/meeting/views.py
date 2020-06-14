from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

from .models import Meeting, Room


# Create your views here.


def details(request, id):  # here we want to get the meeting details based on ID
    # meeting = Meeting.objects.get(pk=id)
    # in case use look for meeting id that doesn't exist
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meeting/details.html', {"meeting": meeting})


def room_detail(request, id):
    meeting_room = Room.objects.get(pk=id)
    return render(request, 'meeting/room_detail.html', {"room": meeting_room})


MeetingForm = modelform_factory(Meeting, exclude=[])


# To create new meeting
def new(request):
    if request.POST:
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, 'meeting/new.html', {"form": form})
