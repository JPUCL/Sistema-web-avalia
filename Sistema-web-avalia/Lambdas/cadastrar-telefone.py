def cadastrar_telefone(pedido):
    """Função para cadastrar um telefone no banco de dados."""
    telefone = pedido.get('telefone')
    # Código para salvar o telefone no banco de dados
    save_database(telefone)
    print(f"Telefone {telefone} cadastrado com sucesso.")