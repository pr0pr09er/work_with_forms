from django.contrib import admin
from django.urls import path
from formApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('makeAppointment/', views.index),
    path('makeAppointment/appointment/', views.appointment),
    path('order/', views.check_order)
]
