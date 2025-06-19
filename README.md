Backend API - Loja de Brinquedos
API RESTful para gerenciamento de clientes e vendas de uma loja de brinquedos, desenvolvida em Python 3.12 com Flask, utilizando PostgreSQL como banco de dados.

Índice
Descrição

Tecnologias

Pré-requisitos

Instalação

Configuração

Execução

Endpoints

Autenticação

Testes

Considerações

Licença

Descrição
Este projeto backend foi construído para avaliar domínio de stack, boas práticas e raciocínio lógico, organizando uma API que:

Permite cadastrar, editar, listar e excluir clientes

Possui filtros por nome e email

Registra vendas associadas a clientes

Retorna estatísticas avançadas: cliente com maior volume de vendas, maior ticket médio e maior frequência de compra

Protege rotas de consulta com autenticação JWT

Utiliza banco PostgreSQL para persistência

Documenta a API com Swagger (via Flask-RESTX)

Possui testes automatizados

Tecnologias
Python 3.12

Flask 3.0

Flask-SQLAlchemy

Flask-Migrate

Flask-JWT-Extended

Flask-RESTX (Swagger)

PostgreSQL

Pytest

python-dotenv

Pré-requisitos
Python 3.12 instalado

PostgreSQL instalado e rodando

Ambiente virtual recomendado (venv)

Instalação
Clone o repositório:

bash
Copiar
Editar
git clone <url-do-repositorio>
cd backend_toy_store
Crie e ative o ambiente virtual:

bash
Copiar
Editar
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configuração
Crie um arquivo .env na raiz do projeto com as variáveis:

ini
Copiar
Editar
DATABASE_URI=postgresql://usuario:senha@localhost:5432/toystore
JWT_SECRET_KEY=segredo_super_secreto
Substitua usuario, senha e toystore pelos seus dados de conexão com PostgreSQL.

Execução
Inicialize o banco e as tabelas com migrations:

bash
Copiar
Editar
flask db init
flask db migrate -m "Criar tabelas cliente e venda"
flask db upgrade
Rode o servidor:

bash
Copiar
Editar
python run.py
A API estará disponível em http://127.0.0.1:5000/.

Endpoints Principais
POST /clientes/ — Cadastrar cliente

GET /clientes/ — Listar clientes (com autenticação)

GET /clientes/<id> — Buscar cliente por ID

PUT /clientes/<id> — Atualizar cliente

DELETE /clientes/<id> — Excluir cliente

Endpoints adicionais para vendas e estatísticas podem ser implementados.

Autenticação
A autenticação é feita via JWT. Para consultar rotas protegidas, o token deve ser enviado no header:

makefile
Copiar
Editar
Authorization: Bearer <seu_token>
Testes
Para rodar os testes automatizados:

bash
Copiar
Editar
pytest
Os testes verificam o cadastro e outras operações básicas da API.

Considerações
API projetada em arquitetura MVC clássica

Tratamento e normalização dos dados esperado para o frontend, considerando dados redundantes na resposta

Foco em código limpo, estrutura clara e documentação automática

Facilita expansão para novas funcionalidades

Licença
Este projeto é open source, sinta-se livre para usar e contribuir.