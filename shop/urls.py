from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu,name="menu"),
    path('catalogos/', views.catalogos, name='catalogos'),
    path('erro/', views.erro, name='erro'),
    path('gerencias/', views.gerencias, name='gerencias'),
    path('catalogo/<int:pk>/', views.catalogo, name='catalogo'),
    path('gerencia/<int:pk>/', views.gerencia, name='gerencia'),
    path('compra/<int:pk>/', views.compra, name='compra'),
    path('edicao/<int:pk>/', views.edicao, name='edicao'),

    path('final/<int:arg>/', views.final, name='final'),

    path('gerencias/adiciona/', views.adiciona, name='adiciona'),
    


]