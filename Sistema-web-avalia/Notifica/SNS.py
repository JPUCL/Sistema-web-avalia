def enviar_sms_ou_push(usuario, mensagem):
    """Função para enviar SMS ou Push Notification via SNS."""
    sns_client = boto3.client('sns')

    # Se o usuário tiver um número de telefone, envia SMS
    if usuario.get('telefone'):
        response = sns_client.publish(
            PhoneNumber=usuario['telefone'],
            Message=mensagem
        )
        print(f"Notificação SMS enviada para {usuario['nome']}")
    
    # Se não, envia Push Notification (implementação fictícia para push)
    elif usuario.get('device_token'):
        response = sns_client.publish(
            TargetArn=usuario['device_token'],
            Message=mensagem
        )
        print(f"Notificação Push enviada para {usuario['nome']}")
    else:
        print("Usuário sem dados para envio de notificação.")