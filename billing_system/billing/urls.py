from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('bill', views.bill, name='bill'),
    path('end', views.end, name='end'),
    path('payment', views.payment, name='payment'),
    path('testform', views.bill, name='testform'),

]

urlpatterns += staticfiles_urlpatterns()
