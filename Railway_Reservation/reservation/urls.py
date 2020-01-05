from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.reservation, name= 'reservation'),
    path('report', views.report, name= 'report'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('admin/', admin.site.urls),
]