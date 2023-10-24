from confluent_kafka import Consumer
from model.ordem_servico import OrdemServicoModel
from db.db import add_Ordem

consumer = Consumer(
    {
        "bootstrap.servers": "broker:29092",
        "group.id": "seu_grupo",
        "auto.offset.reset": "earliest",
    }
)


def consumir_mensagens():
    consumer.subscribe(["grpc"])
    print("consumer on")
    while True:
        msg = consumer.poll(timeout=1000)
        if msg is None:
            continue
        if msg.error():
            print(f"Erro ao consumir mensagem: {msg.error()}")
            continue
        print(f'Consumer: Nova mensagem: {msg.value().decode("utf-8")}')
        msgJson = msg.value().decode("utf-8")
        print(msgJson)
        ordemServicoModel = OrdemServicoModel.json_para_ordem_servico(msgJson)
        print(ordemServicoModel)
        add_Ordem(ordemServicoModel)
