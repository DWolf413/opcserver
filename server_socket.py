import socket
import json
from opc

def obtencion_de_paramentros(datos_telefono):
    print(datos_telefono['Extension'])


mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000))
mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    data = conexion.recv(1024)
    datos_telefono = data.decode()
    datos_telefono = json.loads(data) 
    #print(datos_telefono)
    obtencion_de_paramentros(datos_telefono)
    message = ("Datos recibido").encode()
    conexion.sendall(message)
    conexion.close()
