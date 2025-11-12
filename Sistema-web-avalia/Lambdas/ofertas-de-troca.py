def ver_ofertas_de_troca(pedido):
    """Função para retornar as ofertas de troca disponíveis para o usuário."""
    usuario = pedido.get('usuario')
    ofertas = buscar_ofertas_no_banco(usuario)
    return ofertas

def buscar_ofertas_no_banco(usuario):
    """Busca as ofertas de troca para um usuário no banco de dados."""
    # Exemplo de consulta ao banco de dados
    ofertas = [{"modelo": "iPhone 13", "estado": "novo"}, {"modelo": "Samsung S21", "estado": "usado"}]
    return ofertas