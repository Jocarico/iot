"""
@author J.Rico
@since 2022-05-10
@descrip Ejercicio de Flask
"""

# Inclusion de modulos

from crypt import methods
from flask import Flask, request

app = Flask('__main__')

@app.route('/')
def go_main():
    return "Hello world!"
    


device = {
    "code": "12312414",
    "descrip": "Temp, sensor",
    "value": 67
}

@app.route('/devices', methods=['GET'])
def go_home():
    return device
    
    #Save an user
@app.route('/users', methods=['POST'])
def save_users():
    user = request.json
    print(user)
    return user
    
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device, 201



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
