import grpc
from concurrent import futures
from server.services.grpc_service_impl import MeuServicoImpl
import server.proto.meu_servico_pb2_grpc as meu_servico_pb2_grpc
from messages.kafka_consumer import consumir_mensagens


def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meu_servico_pb2_grpc.add_MeuServicoServicer_to_server(MeuServicoImpl(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Servidor gRPC iniciado na porta 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    import threading

    threading.Thread(target=consumir_mensagens, daemon=True).start()
    run_server()

# PARA RODAR O SERVIDOR USAR NO PROMPT: python3 servidor.py
