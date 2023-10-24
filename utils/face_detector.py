import cv2
import mediapipe as mp
import os
import datetime
MARGIN = 15  # pixels
ROW_SIZE = 10  # pixels
RED = 0, 0, 255

def detectar_e_marcar_rostos(caminho_imagem, pasta_destino):
    # Inicializa o MediaPipe
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

    # Carrega a imagem
    image = cv2.imread(caminho_imagem)

    # Detecta rostos
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Cria a pasta de destino se ela não existir
    os.makedirs(pasta_destino, exist_ok=True)
    print(results)
    # Desenha os marcadores e salva os rostos recortados
    for i, detection in enumerate(results.detections):
        bboxC = detection.location_data.relative_bounding_box
        print(bboxC)
        ih, iw, _ = image.shape
        x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

        offSet = 0.25
        offSetX = int (w * offSet)
        offSetY = int (h * offSet)
        

        # Recorta o rosto
        rosto_recortado = image[y-offSetY:y+h+offSetY, x-offSetX:x+w+offSetX]
        data = datetime.datetime.now()
        # Define o caminho de destino para o rosto recortado
        caminho_destino = os.path.join(pasta_destino, f'rosto_{i}_{data.second}.jpg')
        # Salva o rosto como uma imagem separada
        cv2.imwrite(caminho_destino, rosto_recortado)

    # Retorna a imagem com os marcadores
    return image
