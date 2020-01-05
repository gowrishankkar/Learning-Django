from django.http import HttpResponse
from django.shortcuts import render
from reservation.forms import ReservationForm
import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return HttpResponse("Hello, world. You're at reservation")

# def reservation(request):
#     x = []
#     for i in range(10):
#         x.append(i)
#     return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))

def reservation(request):
    return render(request, 'base.html')

def report(request):
    return render(request, "report.html")

def get(self, request):
    form = ReservationForm()
    return render(request, "report.html", {'form': form})