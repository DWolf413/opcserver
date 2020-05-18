import socket
import json
from opcua.crypto import uacrypto
from opcua import Server, ua
import time


def obtencion_de_paramentros(datos_telefono):
    print(datos_telefono['Extension'])
    
    datos_telefono['Extension'] = node.add_object(addspace, datos_telefono['Extension'])
    datos_telefono['Interfono'] = datos_telefono['Extension'].add_object(addspace, datos_telefono['Interfono'])
    
    
    
    
    
    #estacion = interfono.add_object(addspace, "Estacion")
    #id_telefono = estacion.add_variable(addspace, 'Id', datos_telefono['id'])
    #registro = estacion.add_variable(addspace, 'Registro', datos_telefono['Registro'])
    #estado = estacion.add_variable(addspace, 'Estado', datos_telefono['Estado'])
    #llamada = estacion.add_variable(addspace, 'Llamada', datos_telefono['Llamada'])
    #linea = estacion.add_variable(addspace, 'Linea', datos_telefono['Linea'])

    #id_telefono.set_writable()
    #registro.set_writable()
    #estado.set_writable()
    #llamada.set_writable()
    #linea.set_writable()

    
    #id_telefono.set_value(datos_telefono['id'])
    #registro.set_value(datos_telefono['Registro'])
    #estado.set_value(datos_telefono['Estado'])
    #llamada.set_value(datos_telefono['Llamada'])
    #linea.set_value(datos_telefono['Linea'])

    

   #escritura_de_parametros(datos_telefono)

def comprobacion(datos_linea, lista_lineas):

    for lineas in lista_lineas:
        if lineas == datos_telefono['Linea']:
            print('Encontrado')
        break




if __name__ == '__main__':

    #PAREMETROS
    lista_lineas = [] 
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
    server.start()


while True:
    conexion, addr = mi_socket.accept()
    data = conexion.recv(1024)
    datos_telefono = data.decode()
    datos_telefono = json.loads(data) 
    lista_lineas.append(datos_telefono['Linea'])
    comprobacion(datos_telefono, lista_lineas)


    #obtencion_de_paramentros(datos_telefono)
    #print('OPC ENCENDIDO')
    #message = ("Datos recibido").encode()
    #conexion.sendall(message)
    conexion.close()
