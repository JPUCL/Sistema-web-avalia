import boto3

sns_client = boto3.client('sns')

def salvar_notificacao_fila(usuario):
    """Salvar a notificação na fila para envio posterior."""
    mensagem = f"Olá, {usuario['nome']}! Temos novas ofertas de troca para você."
    # Adiciona a notificação na fila de notificações
    notificacao = {
        'usuario': usuario,
        'mensagem': mensagem
    }
    enviar_notificacao(notificacao)

def enviar_notificacao(notificacao):
    """Função para enviar a notificação via SNS (SMS, push, etc.)."""
    usuario = notificacao['usuario']
    mensagem = notificacao['mensagem']
    
    # Supondo que o usuário tenha um número de telefone registrado para SMS
    phone_number = usuario.get('telefone')
    
    if phone_number:
        response = sns_client.publish(
            PhoneNumber=phone_number,
            Message=mensagem
        )
        print(f"Notificação enviada: {response}")
    else:
        print("Usuário sem número de telefone registrado para SMS.")