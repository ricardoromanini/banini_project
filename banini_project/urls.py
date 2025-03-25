from django.contrib import admin
from django.urls import path
from banini_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pagamentos/', views.lista_pagamentos, name='lista_pagamentos'),
    path('pagamentos/baixa/<int:id>/', views.baixa_pagamento, name='baixa_pagamento'),
]
