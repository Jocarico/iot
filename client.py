from email import header
from http import client
from wsgiref import headers
from iiot_device import Sensor
import json
import time


# Creacion de un objeto de la clase HTTPConnection
_conn = client.HTTPConnection(host='localhost', port=5000)

# Creacion de un objeto de la clase Sensor
s = Sensor()
# Etiqueta para informar que el tipo de dato es JSON
h = {'Content-type':'application/json'}
while True:

    data = {
        'id': 1,
        'name': 'Temp sensor: ',
        'value': s.get_random_number()
    }

    json_data = json.dumps(data)

    _conn.request('POST','/devices', json_data, headers=h)
    _conn.close()



    print(s.get_random_number())
    # rint(s.get_temp())
    time.sleep(1)
