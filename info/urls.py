from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalle/<int:index>/', views.detalle, name='detalle'),
    path('eliminar_nave/<str:puerto>/<int:idx>/', views.eliminar_nave, name='eliminar_nave'),
    path('seleccionar-naves/', views.seleccionar_naves, name='seleccionar_naves'),
    path('check_updates/', views.check_updates, name='check_updates'),
    path('descargar_excel/', views.descargar_excel, name='descargar_excel'),
]
