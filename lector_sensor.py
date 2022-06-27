from distutils.command.upload import upload
from email.contentmanager import raw_data_manager
import serial
import time

#pyserial.org Documentation
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# 

while True:
    raw_data = ser.readline()
    # data = float(raw_data[0])
    print(raw_data)
    time.sleep(1)

ser.close()