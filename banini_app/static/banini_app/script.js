function abrirModalBaixa(id, valor) {
    document.getElementById('modalBaixa').style.display = 'block';
    document.getElementById('formBaixa').action = '/baixa_pagamento/' + id + '/';
    document.getElementById('data_pagamento').valueAsDate = new Date();
    document.getElementById('valor_pago').value = valor;
}
function fecharModal() {
    document.getElementById('modalBaixa').style.display = 'none';
}