from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    #path('machines/', views.machine_list_view, name='machines'),
]