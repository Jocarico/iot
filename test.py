from os import remove


while True:
    arduinoData = input("Data: ")
    try:
        arduinoData= arduinoData.replace('"', '')
        arduinoData= arduinoData.replace("'", '')

        if arduinoData == "True": arduinoData = 1
        if arduinoData == "False": arduinoData = 0

        arduinoData= float(arduinoData)
        arduinoData = int(arduinoData)
        print("El dato esta nombrado como numero. Feliz")
        break
    except ValueError:
        print("Introduce un dato numerico entero, no agregues comilla(s)")
        continue
 
print(arduinoData)
if type(arduinoData) == int :
    print("El dato esta nombrado como numero.")
    
else:
    print("No workea")
