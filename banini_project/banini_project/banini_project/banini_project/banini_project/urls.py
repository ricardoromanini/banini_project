
from django.contrib import admin
from django.urls import path
from banini_app import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/novo/', views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('fornecedores/editar/<int:fornecedor_id>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('fornecedores/excluir/<int:fornecedor_id>/', views.excluir_fornecedor, name='excluir_fornecedor'),
    path('pagamentos/', views.listar_pagamentos, name='listar_pagamentos'),
    path('pagamentos/novo/', views.cadastrar_pagamento, name='cadastrar_pagamento'),
    path('pagamentos/baixa/<int:pagamento_id>/', views.baixar_pagamento, name='baixar_pagamento'),
]
