
from django.contrib import admin
from django.urls import path
from banini_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pagamentos/', views.lista_pagamentos, name='lista_pagamentos'),
    path('pagamentos/novo/', views.novo_pagamento, name='novo_pagamento'),
    path('pagamentos/baixa/<int:pagamento_id>/', views.baixa_pagamento, name='baixa_pagamento'),
    path('fornecedores/', views.lista_fornecedores, name='lista_fornecedores'),
    path('fornecedores/novo/', views.novo_fornecedor, name='novo_fornecedor'),
    path('fornecedores/novo-modal/', views.novo_fornecedor_modal, name='novo_fornecedor_modal'),
    path('relatorios/', views.gerar_relatorio, name='gerar_relatorio'),
    
    # Esta linha foi comentada porque a view 'dashboard' não existe mais
    # path('dashboard/', views.dashboard, name='dashboard'),
]
