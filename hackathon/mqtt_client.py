import paho.mqtt.client as mqtt
import json
from datetime import datetime

BROKER = "192.168.0.15"   # IP del broker
PORT = 1883

TOPIC = "raton/evento"

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

def publicar_evento(confianza):

    mensaje = {

        "evento": "TRAMPA_ACTIVADA",

        "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "confianza": round(confianza,2)

    }

    client.publish(TOPIC, json.dumps(mensaje))

    print("MQTT enviado")