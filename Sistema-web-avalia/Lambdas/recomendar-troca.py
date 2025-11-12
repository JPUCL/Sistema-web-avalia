def recomendar_troca(pedido):
    """Função para recomendar a troca de telefones entre dois usuários."""
    usuario = pedido.get('usuario')
    telefone = pedido.get('telefone')
    # Lógica para buscar a melhor troca
    recomendacao = {
        'usuario': usuario,
        'recomendacao': f"Recomendado trocar seu {telefone['modelo']} por um iPhone 13."
    }
    return recomendacao