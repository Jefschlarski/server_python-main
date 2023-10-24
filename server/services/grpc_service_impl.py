import server.proto.meu_servico_pb2 as meu_servico_pb2, server.proto.meu_servico_pb2_grpc as meu_servico_pb2_grpc
from utils.face_detector import detectar_e_marcar_rostos
from PIL import Image
from datetime import datetime
from io import BytesIO
import cv2
from messages.kafka_producer import enviar_mensagem

class MeuServicoImpl(meu_servico_pb2_grpc.MeuServicoServicer):
    
    def getImage(self, request, context):
        resposta = 'imagem recebida'
        
        imagem = Image.open(BytesIO(request.image))
        data = datetime.now()
        pasta_destino = ('/home/jeferson/Imagens/')
        imagePatch = (f'/home/jeferson/Imagens/{data}.png')
        imagem.save(imagePatch)
        print(f'Imagem salva com o nome : {data}')

        # Chamar a função para detectar rostos
        imagem_processada = detectar_e_marcar_rostos(imagePatch, pasta_destino)

        # Mostrar a imagem com os rostos detectados
        cv2.imshow('Rostos Detectados', imagem_processada)
        cv2.imwrite(imagePatch, imagem_processada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        return meu_servico_pb2.Resposta(resposta = resposta)
        

    def MetodoOrdemServico(self, request, context):
        print(f"colaborador {request.nome} com o id:{request.id} da prefeitura de {request.local} fez um request")
        
        ordemServicoList = []

        ordem_servico = meu_servico_pb2.OrdemServico(
        id=1, title="Exemplo", geojson="...", lat=12.34, lng=56.78, relator="João", date="2023-10-17", status=True)
        ordemServicoList.append(ordem_servico)

        ordem_servico1 = meu_servico_pb2.OrdemServico(
        id=2, title="Exemplo2", geojson="...", lat=12.342, lng=56.782, relator="João2", date="2024-10-17", status=False)
        ordemServicoList.append(ordem_servico1)

        return meu_servico_pb2.OrdemServicoList(ordemServicoList = ordemServicoList)
    
    #METODO GRPC
    def MeuMetodo(self, request, context):
        resultado = enviar_mensagem(request)
        return meu_servico_pb2.MinhaResposta(resultado=resultado)
    
