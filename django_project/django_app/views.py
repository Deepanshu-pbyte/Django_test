from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

# Create your views here.


def date(request):
    now = datetime.datetime.now()
    time = "Time is {}".format(now)
    return HttpResponse(time)


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
