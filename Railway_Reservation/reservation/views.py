from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at reservation")

# def reservation(request):
#     x = []
#     for i in range(10):
#         x.append(i)
#     return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))


def reservation(request):
    return render(request, 'base.html')


def display(request):
    return render(request, "display.html")


def reserve(request):
    return render(request, "reserve.html")
