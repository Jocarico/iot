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