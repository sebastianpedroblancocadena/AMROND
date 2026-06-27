import serial
import time
from config import SERIAL_PORT, BAUDRATE

arduino = serial.Serial(SERIAL_PORT, BAUDRATE)
time.sleep(2)

def activar_trampa():

    arduino.write(b"TRAP\n")

    print(">>> Servo Activado")