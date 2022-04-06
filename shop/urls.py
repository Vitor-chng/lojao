from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/<int:pk>/', views.pag2, name='pag2'),
    path('post/new/', views.novo, name='novo'),
]