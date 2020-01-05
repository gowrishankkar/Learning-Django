from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path('display', views.display, name='display'),
    path('reserve', views.reserve, name='reserve'),

]

urlpatterns += staticfiles_urlpatterns()
