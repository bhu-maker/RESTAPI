from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [path('list',views.listing),
               path('up/<int:pk>',views.updating),
               path('classlist',views.restlisting.as_view()),
               path('classup/<int:pk>',views.restdetaillisting.as_view())]
