from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting


def welcome(request):
    return render(
        request,
        "website/welcome.html",
        {"meetings": Meeting.objects.all()},
    )


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse(
        "This is a page about me, my name is Eddie and I am a Junior Dev interning at Hometap"
    )


# Create your views here.
