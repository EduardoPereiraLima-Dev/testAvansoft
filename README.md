# 🧸 API Loja de Brinquedos — Backend

API REST desenvolvida em **Python 3.12 com Flask** para gerenciamento de clientes e vendas de uma loja de brinquedos.

A API permite:
- Cadastro de clientes
- Registro de vendas associadas
- Listagem de clientes
- Atualização e exclusão
- Cadastro em lote via JSON estruturado
- Autenticação via JWT

---

## 📌 Tecnologias Utilizadas

- Python 3.12
- Flask
- Flask-RESTX (para versionamento e documentação)
- Flask-JWT-Extended (para autenticação)
- SQLAlchemy (ORM)
- Flask-Migrate (controle de migrations)
- PostgreSQL

---

## 📦 Funcionalidades

✅ Cadastro de clientes com:
- Nome completo
- E-mail  

✅ Registro de vendas associadas:
- Data da venda  
- Valor  

✅ Cadastro de múltiplos clientes com vendas no mesmo payload JSON

✅ Autenticação via JWT  

✅ Listagem, busca, edição e remoção de clientes

---

## 📑 Exemplo de JSON para Cadastro em Lote

```json
{
  "data": {
    "clientes": [
      {
        "info": {
          "nomeCompleto": "Ana Beatriz",
          "detalhes": {
            "email": "ana.b@example.com"
          }
        },
        "estatisticas": {
          "vendas": [
            { "data": "2024-01-01", "valor": 150 },
            { "data": "2024-01-02", "valor": 50 }
          ]
        }
      }
    ]
  }
}
