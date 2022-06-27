from email import header
from http import client
from wsgiref import headers
from iiot_device import Sensor
import json
import time
from distutils.command.upload import upload
from email.contentmanager import raw_data_manager
import serial

#pyserial.org Documentation
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)


# Creacion de un objeto de la clase HTTPConnection
_conn = client.HTTPConnection(host='localhost', port=5000)

# Creacion de un objeto de la clase Sensor
s = Sensor()
# Etiqueta para informar que el tipo de dato es JSON
h = {'Content-type':'application/json'}
while True:
    raw_data = ser.readline()
    # data = float(raw_data[0])
    arduinoData= bytes.decode(raw_data)
    
    if (type(arduinoData) != int or type(arduinoData) != float):
        print("El dato no esta nombrado como numero.")
    else:

        time.sleep(1)


        data = {
            'id': 1,
            'name': 'inclinacion en grados: ',
            'value': arduinoData,
            'value2': s.get_random_number()

        }
        print(data)

        json_data = json.dumps(data)

        _conn.request('POST','/devices', json_data, headers=h)
        _conn.close()



        print(s.get_random_number())
        # rint(s.get_temp())
        time.sleep(1)
    ser.close()
