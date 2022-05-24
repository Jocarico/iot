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
        return randint(0, 100)