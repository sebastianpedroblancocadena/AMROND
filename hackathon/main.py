import cv2
import time

from detector import detectar
from arduino import activar_trampa
from mqtt_client import publicar_evento

from config import *

cap = cv2.VideoCapture(CAMERA_ID)

inicio_deteccion = None

cooldown = False

ultimo_disparo = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    detectado, confianza, imagen = detectar(
        frame,
        CONFIDENCE,
        IMG_SIZE
    )

    ahora = time.time()

    if cooldown:

        if ahora - ultimo_disparo > COOLDOWN:

            cooldown = False

    if detectado and not cooldown:

        if inicio_deteccion is None:

            inicio_deteccion = ahora

        tiempo = ahora - inicio_deteccion

        cv2.putText(
            imagen,
            f"Detectando: {tiempo:.1f}s",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        if tiempo >= DETECTION_TIME:

            print("RATON CONFIRMADO")

            activar_trampa()
            publicar_evento(confianza)

            cooldown = True

            ultimo_disparo = time.time()

            inicio_deteccion = None

    else:

        inicio_deteccion = None

    if cooldown:

        restante = COOLDOWN - (time.time()-ultimo_disparo)

        cv2.putText(
            imagen,
            f"Cooldown: {int(restante)}",
            (20,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2
        )

    cv2.imshow("Mouse Trap AI", imagen)

    if cv2.waitKey(1)==27:
        break

cap.release()

cv2.destroyAllWindows()