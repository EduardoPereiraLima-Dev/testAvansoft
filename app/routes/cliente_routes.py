from flask_restx import Resource, Namespace
from flask import request
from app.controllers import cliente_controller
from flask_jwt_extended import jwt_required

clientes_ns = Namespace('clientes', description='Operações de clientes')

@clientes_ns.route('/')
class ClienteListResource(Resource):
    @jwt_required()
    def get(self):
        clientes = cliente_controller.listar_clientes()
        return [{'id': c.id, 'nome': c.nome_completo, 'email': c.email} for c in clientes]

    @jwt_required()
    def post(self):
        dados = request.get_json()
        clientes = cliente_controller.cadastrar_clientes_em_lote(dados)
        ids = [c.id for c in clientes]
        return {'clientes_criados': ids}, 201
