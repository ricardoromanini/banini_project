from django.shortcuts import render, get_object_or_404, redirect
from .models import Pagamento, Fornecedor
from django.utils.timezone import now
from datetime import timedelta
from django.http import JsonResponse
from .forms import PagamentoForm

def home(request):
    hoje = now().date()
    proximos_3_dias = hoje + timedelta(days=3)
    
    pagamentos_vencidos = Pagamento.objects.filter(pago=False, data_vencimento__lt=hoje)
    pagamentos_proximos = Pagamento.objects.filter(pago=False, data_vencimento__range=(hoje, proximos_3_dias))
    pagamentos_futuros = Pagamento.objects.filter(pago=False, data_vencimento__gt=proximos_3_dias)

    return render(request, 'banini_app/home.html', {
        'pagamentos_vencidos': pagamentos_vencidos,
        'pagamentos_proximos': pagamentos_proximos,
        'pagamentos_futuros': pagamentos_futuros,
    })

def baixa_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method == 'POST':
        pagamento.pago = True
        pagamento.data_pagamento = request.POST.get('data_pagamento')
        pagamento.valor_pago = request.POST.get('valor_pago')
        pagamento.forma_pagamento = request.POST.get('forma_pagamento')
        pagamento.save()
        return redirect('/')
    return JsonResponse({'erro': 'Requisição inválida'}, status=400)

def dashboard(request):
    return render(request, 'banini_app/dashboard.html')
