from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [path('list',views.listing),
               path('up/<int:pk>',views.updating),
               path('api/postt',views.apilisting),
               path('api/gett',views.apigetting),
               path('api/gett/<para>',views.apireading),
               path('classlist',views.restlisting.as_view()),
               path('classup/<int:pk>',views.restdetaillisting.as_view())]
