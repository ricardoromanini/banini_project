from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('lista_pagamentos')),  # Redireciona a / para lista de pagamentos
    path('pagamentos/', include('banini_app.urls')),         # Inclui as rotas da sua aplicação
]