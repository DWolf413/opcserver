import socket
import json
from opcua.crypto import uacrypto
from opcua import Server, ua


def obtencion_de_paramentros(datos_telefono):
    print(datos_telefono['Extension'])
    Parametros = node.add_object(addspace, datos_telefono['Extension'])

if __name__ == '__main__':

    #ACTIVACIÓN SERVIDOR SOCKET
    mi_socket = socket.socket()
    mi_socket.bind(('localhost', 8000))
    mi_socket.listen(5)

    #ACTIVACION SERVIDOR OPC
    server = Server()
    url = 'opc.tcp://192.168.100.6:4840'
    server.set_endpoint(url)

    name = "OPCUA_SERVER"
    addspace = server.register_namespace(name)

    node = server.get_objects_node()


while True:
    conexion, addr = mi_socket.accept()
    data = conexion.recv(1024)
    datos_telefono = data.decode()
    datos_telefono = json.loads(data) 
    #print(datos_telefono)
    obtencion_de_paramentros(datos_telefono)
    server.start()
    print('OPC ENCENDIDO')
    message = ("Datos recibido").encode()
    conexion.sendall(message)
    conexion.close()
