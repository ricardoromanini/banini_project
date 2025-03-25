
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Fornecedor, Pagamento
from .forms import FornecedorForm, PagamentoForm, BaixaPagamentoForm


def home(request):
    hoje = date.today()
    proximos_3_dias = hoje + timedelta(days=3)

    pagamentos = Pagamento.objects.filter(pago=False).order_by('data_vencimento')
    vencidos = pagamentos.filter(data_vencimento__lt=hoje)
    proximos = pagamentos.filter(data_vencimento__gte=hoje, data_vencimento__lte=proximos_3_dias)
    futuros = pagamentos.filter(data_vencimento__gt=proximos_3_dias)

    total_pago_mes = Pagamento.objects.filter(
        pago=True,
        data_pagamento__month=hoje.month,
        data_pagamento__year=hoje.year
    ).aggregate(total=Sum('valor_pago'))['total'] or 0

    total_vencido = vencidos.aggregate(total=Sum('valor'))['total'] or 0
    total_a_vencer = proximos.aggregate(total=Sum('valor'))['total'] or 0

    context = {
        'vencidos': vencidos,
        'proximos': proximos,
        'futuros': futuros,
        'total_pago_mes': total_pago_mes,
        'total_vencido': total_vencido,
        'total_a_vencer': total_a_vencer,
    }
    return render(request, 'home.html', context)

def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'listar_fornecedores.html', {'fornecedores': fornecedores})

def cadastrar_fornecedor(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_fornecedores')
    return render(request, 'cadastrar_fornecedor.html', {'form': form})

def editar_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    if form.is_valid():
        form.save()
        return redirect('listar_fornecedores')
    return render(request, 'editar_fornecedor.html', {'form': form})

def excluir_fornecedor(request, fornecedor_id):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('listar_fornecedores')
    return render(request, 'excluir_fornecedor.html', {'fornecedor': fornecedor})

def cadastrar_pagamento(request):
    form = PagamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pagamentos')
    return render(request, 'cadastrar_pagamento.html', {'form': form})

def listar_pagamentos(request):
    pagamentos = Pagamento.objects.select_related('fornecedor').all()
    return render(request, 'listar_pagamentos.html', {'pagamentos': pagamentos})

def baixar_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, id=pagamento_id)
    form = BaixaPagamentoForm(request.POST or None, instance=pagamento)
    if form.is_valid():
        baixa = form.save(commit=False)
        baixa.pago = True
        baixa.save()
        return redirect('listar_pagamentos')
    return render(request, 'baixa_pagamento.html', {'form': form, 'pagamento': pagamento})

from django.db.models import Sum, Count
from datetime import date
from django.utils.timezone import now
from calendar import month_name
from collections import defaultdict

def dashboard(request):
    hoje = date.today()

    # Pagamentos do mês atual
    pagamentos_mes = Pagamento.objects.filter(data_vencimento__month=hoje.month, data_vencimento__year=hoje.year)

    total_pago_mes = pagamentos_mes.filter(pago=True).aggregate(total=Sum('valor_pago'))['total'] or 0
    total_vencido = Pagamento.objects.filter(pago=False, data_vencimento__lt=hoje).aggregate(total=Sum('valor'))['total'] or 0
    total_a_vencer = Pagamento.objects.filter(pago=False, data_vencimento__gte=hoje).aggregate(total=Sum('valor'))['total'] or 0

    # Gráfico de pagamentos por status
    status_data = {
        'Pago': Pagamento.objects.filter(pago=True).count(),
        'A Vencer': Pagamento.objects.filter(pago=False, data_vencimento__gte=hoje).count(),
        'Vencido': Pagamento.objects.filter(pago=False, data_vencimento__lt=hoje).count(),
    }

    # Gastos mensais por mês (últimos 6 meses)
    from datetime import timedelta
    from django.db.models.functions import TruncMonth

    ultimos_meses = Pagamento.objects.filter(data_vencimento__lte=hoje).annotate(
        mes=TruncMonth('data_vencimento')
    ).values('mes').annotate(total=Sum('valor')).order_by('mes')

    meses = []
    totais = []
    for item in ultimos_meses:
        meses.append(item['mes'].strftime("%b/%Y"))
        totais.append(float(item['total']))

    context = {
        'total_pago_mes': total_pago_mes,
        'total_vencido': total_vencido,
        'total_a_vencer': total_a_vencer,
        'status_labels': list(status_data.keys()),
        'status_values': list(status_data.values()),
        'meses': meses,
        'totais': totais,
    }
    return render(request, 'dashboard.html', context)
