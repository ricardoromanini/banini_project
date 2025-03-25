from django.shortcuts import render
from datetime import datetime, timedelta

def home(request):
    hoje = datetime.now().date()
    proximos_3_dias = hoje + timedelta(days=3)
    return render(request, 'home.html', {'hoje': hoje, 'proximos_3_dias': proximos_3_dias})

def lista_pagamentos(request):
    return render(request, 'lista_pagamentos.html')

def baixa_pagamento(request, id):
    return render(request, 'baixa_pagamento.html', {'id': id})
