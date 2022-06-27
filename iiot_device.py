from distutils.command.upload import upload
import serial
from email.contentmanager import raw_data_manager
from random import randint
#psutil almacena datos del hardware
# import psutil

#Definicion de la clase

class Sensor:

    # Constructor de la clase
    def __init__(self):
       # self._sensor = psutil.sensors_temperatures()
       pass
    
    def get_temp(self):
        return self._sensor['coretemp']
    # Simulacion toma de valor de otro sensor
    def get_random_number(self):
        grades = randint(0,50)
        if grades > 15:
            grados = str(grades)
            print("Plancha desnivelada por: "+ grados + "grados")
        else:
            grados = str(grades)
            print("Plancha nivelada. "+ grados + "grados")
        return grades

    def get_temperature(self):
        #pyserial.org Documentation
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

        # 

        while True:
            raw_data = ser.readline()
            # data = float(raw_data[0])
            return raw_data