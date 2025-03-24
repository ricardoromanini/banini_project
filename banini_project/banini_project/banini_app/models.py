
from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj_cpf = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    TIPO_GASTO_CHOICES = [('fixo', 'Fixo'), ('variavel', 'Variável')]
    RECORRENCIA_CHOICES = [('unico', 'Único'), ('mensal', 'Mensal'), ('quinzenal', 'Quinzenal'), ('semanal', 'Semanal')]

    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    data_vencimento = models.DateField()
    forma_pagamento = models.CharField(max_length=50)
    tipo_gasto = models.CharField(max_length=10, choices=TIPO_GASTO_CHOICES)
    recorrencia = models.CharField(max_length=10, choices=RECORRENCIA_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)
    data_pagamento = models.DateField(null=True, blank=True)
    forma_pagamento_baixa = models.CharField(max_length=50, null=True, blank=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.fornecedor.nome} - {self.data_vencimento}"
