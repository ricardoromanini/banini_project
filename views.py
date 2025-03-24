from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from .models import Pagamento
from .forms import BaixaPagamentoForm

def home(request):
    hoje = datetime.now().date()
    proximos_3_dias = hoje + timedelta(days=3)
    pagamentos_proximos = Pagamento.objects.filter(data_vencimento__range=[hoje, proximos_3_dias], status='pendente')
    return render(request, 'home.html', {'pagamentos_proximos': pagamentos_proximos})

def lista_pagamentos(request):
    pagamentos = Pagamento.objects.all().order_by('-data_vencimento')
    return render(request, 'pagamentos/lista.html', {'pagamentos': pagamentos})

def baixa_pagamento(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    if request.method == 'POST':
        form = BaixaPagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.status = 'pago'
            pagamento.save()
            return redirect('lista_pagamentos')
    else:
        form = BaixaPagamentoForm(instance=pagamento)
    return render(request, 'pagamentos/baixa_pagamento.html', {'form': form, 'pagamento': pagamento})
