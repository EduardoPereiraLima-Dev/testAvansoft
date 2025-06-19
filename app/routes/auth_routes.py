from flask_restx import Resource, Namespace
from flask import request
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth_ns = Namespace('auth', description='Autenticação')

@auth_ns.route('/login/')
class LoginResource(Resource):
    def post(self):
        dados = request.get_json()
        email = dados.get("email")
        senha = dados.get("senha")

        if not email or not senha:
            return {"msg": "Email e senha obrigatórios"}, 400

        # Aqui poderia validar usuário no banco. Simulação fixa:
        access_token = create_access_token(
            identity=email,
            expires_delta=timedelta(minutes=30)
        )

        return {"access_token": access_token}, 200
