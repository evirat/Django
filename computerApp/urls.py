from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',  views.index, name='index'),
    path('machines/', views.machine_list_view, name='machines'),
    path('machines/<pk>', views.machine_detail_views, name='machine-detail'),
    path('add-machine',  views.machine_add_form, name='add-machine'),
    path('machines/<pk>/delete/', views.machine_delete_views, name='machine-delete'),
    path('personnes/', views.personne_list_view, name='personnes'),
    path('personnes/<pk>', views.personne_detail_views, name='personne-detail'),
    path('add-personne',  views.personne_add_form, name='add-personne'),
    path('personnes/<pk>/delete/', views.personne_delete_views, name='personne-delete'),
    path('infrastructures/', views.infrastructures, name='infrastructures'),
    path('add-infrastructure/', views.add_infrastructure, name='add-infrastructure'),
    path('infrastructures/<int:infrastructure_id>/delete/', views.delete_infrastructure, name='delete-infrastructure'),
    path('infrastructure/<int:infrastructure_id>/', views.infrastructure_details, name='infrastructure-details'),
    path('coms/', views.commu_list_view, name='coms'),
    path('coms/<pk>', views.commu_detail_views, name='com-detail'),
    path('add-com',  views.commu_add_form, name='add-com'),
    path('coms/<pk>/delete/', views.commu_delete_views, name='com-delete'),
    path('maintenances/', views.maintenance_list_views, name='maintenances'),
    path('add-maintenance', views.create_maintenance_views, name='add-maintenance'),
]