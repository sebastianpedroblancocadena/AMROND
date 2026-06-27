from ultralytics import YOLO
from config import MODEL_PATH

model = YOLO(MODEL_PATH)

def detectar(frame, conf, imgsz):

    results = model.predict(
        source=frame,
        conf=conf,
        imgsz=imgsz,
        verbose=False
    )

    deteccion = len(results[0].boxes) > 0

    imagen = results[0].plot()

    confianza = 0

    if deteccion:

        confianza = float(results[0].boxes[0].conf)

    return deteccion, confianza, imagen