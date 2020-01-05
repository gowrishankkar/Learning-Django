from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('display', views.display, name='display'),
    path('reserve', views.reserve, name='reserve'),

]
