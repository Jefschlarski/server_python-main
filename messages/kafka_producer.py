from confluent_kafka import Producer

conf = {
    "bootstrap.servers": "broker:29092",  # Adapte para o seu ambiente Kafka
}
# INICIA O PRODUCER
producer = Producer(conf)


def enviar_mensagem(request):
    resultado = None

    def Delivery(err, msg):
        nonlocal resultado
        if err is not None:
            print(f"Erro ao enviar a mensagem: {err}")
            resultado = f"Erro ao enviar a mensagem: {err}"
        else:  # RETORNA UMA RESPOSTA PARA O CLIENTE
            print(f"Mensagem enviada com sucesso para o tópico: {msg.topic()}")
            resultado = f"Mensagem enviada com sucesso para o tópico: {msg.topic()}"

    # ENVIA O EVENDO PRO KAFKA
    producer.produce(
        "grpc", value=f"{request.campo1} {request.campo2}", callback=Delivery
    )
    producer.flush()
    return resultado
