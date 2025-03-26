from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pagamentos, name='lista_pagamentos'),
    path('', views.home, name='home'),
]
