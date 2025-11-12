from queue import Queue

# Fila de pedidos
fila_sqs = Queue()

def salvar_pedido_fila(pedido):
    """Adicionar um pedido na fila SQS para processamento posterior."""
    fila_sqs.put(pedido)
    print(f"Pedido adicionado na fila: {pedido}")

def processar_pedido_fila():
    """Processar pedidos na fila e executar as funções necessárias."""
    while True:
        if not fila_sqs.empty():
            pedido = fila_sqs.get()
            print(f"Processando pedido: {pedido}")
            fila_sqs.task_done()
            processar_pedido(pedido)