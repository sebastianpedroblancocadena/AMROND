# -----------------------------
# CONFIGURACION GENERAL
# -----------------------------

# Modelo YOLO
MODEL_PATH = "best_mouse.pt"

# Camara
CAMERA_ID = 0

# Deteccion
CONFIDENCE = 0.80
IMG_SIZE = 640

# Tiempo que debe mantenerse detectado
DETECTION_TIME = 3.0

# Tiempo para volver a permitir otra activacion
COOLDOWN = 30

# Arduino
SERIAL_PORT = "/dev/ttyACM0"
BAUDRATE = 9600