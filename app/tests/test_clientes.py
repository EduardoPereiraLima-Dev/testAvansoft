def test_cadastro_cliente(client):
    response = client.post('/clientes/', json={
        'nome_completo': 'João da Silva',
        'email': 'joao@example.com',
        'nascimento': '1990-01-01'
    })
    assert response.status_code == 201
