from datetime import datetime
from app.models.cliente import Cliente, Venda
from app.extensions import db

def cadastrar_clientes_em_lote(dados):
    clientes_json = dados.get("data", {}).get("clientes", [])
    clientes_criados = []

    for cliente_json in clientes_json:
        info = cliente_json.get("info", {})
        nome = info.get("nomeCompleto")
        detalhes = info.get("detalhes", {})
        email = detalhes.get("email")

        if not nome or not email:
            continue

        cliente = Cliente(nome_completo=nome, email=email)
        db.session.add(cliente)
        db.session.flush()  # já pega o ID gerado

        estatisticas = cliente_json.get("estatisticas", {})
        vendas = estatisticas.get("vendas", [])
        for venda in vendas:
            data_venda = venda.get("data")
            valor = venda.get("valor")
            if data_venda and valor is not None:
                data_obj = datetime.strptime(data_venda, "%Y-%m-%d").date()
                venda_obj = Venda(cliente_id=cliente.id, data=data_obj, valor=valor)
                db.session.add(venda_obj)

        clientes_criados.append(cliente)

    db.session.commit()
    return clientes_criados
