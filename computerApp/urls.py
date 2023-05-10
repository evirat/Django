from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('machines/', views.machine_list_view, name='machines'),
    path('machines/<pk>', views.machine_detail_views, name='machine-detail'),
    path('add-machine',  views.machine_add_form, name='add-machine'),
    path('machines/<pk>/delete/', views.machine_delete_views, name='machine-delete'),
]