from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.http import HttpResponse

def home(request):
    hoje = datetime.today()
    proximos_3_dias = hoje + timedelta(days=3)
    return HttpResponse(f"Bem-vindo! Hoje é {hoje.strftime('%d/%m/%Y')}")

def lista_pagamentos(request):
    return HttpResponse("Lista de pagamentos (em construção)")

def baixa_pagamento(request, id):
    return HttpResponse(f"Baixa do pagamento ID {id} (em construção)")
