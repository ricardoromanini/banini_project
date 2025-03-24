
from django import forms
from .models import Fornecedor, Pagamento

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj_cpf', 'telefone', 'email']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['fornecedor', 'data_vencimento', 'forma_pagamento', 'tipo_gasto', 'recorrencia', 'valor']

class BaixaPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['data_pagamento', 'forma_pagamento_baixa', 'valor_pago']
