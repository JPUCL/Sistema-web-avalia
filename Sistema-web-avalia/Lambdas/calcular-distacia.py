def calcular_distancia(pedido):
    """Função para calcular a distância entre dois usuários."""
    usuario_origem = pedido['usuario_origem']
    usuario_destino = pedido['usuario_destino']
    distancia = calcular_distancia_geografica(usuario_origem, usuario_destino)
    return distancia

def calcular_distancia_geografica(usuario_origem, usuario_destino):
    """Calcula a distância geográfica entre dois usuários."""
    # Lógica simplificada de cálculo de distância
    lat_origem, lon_origem = usuario_origem['localizacao']
    lat_destino, lon_destino = usuario_destino['localizacao']
    distancia = abs(lat_origem - lat_destino) + abs(lon_origem - lon_destino)
    return distancia