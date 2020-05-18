import socket
import json
from opcua.crypto import uacrypto
from opcua import Server, ua
import time


def creacion_de_parametros(datos_telefono):
    
    linea = node.add_object(addspace, datos_telefono['Extension'])
    estacion = linea.add_object(addspace, datos_telefono['Estacion'])
    interfono = estacion.add_object(addspace, datos_telefono['Interfono'])
    id_telefono = interfono.add_variable(addspace, 'Id', datos_telefono['id'])
    extension = interfono.add_variable(addspace, 'Extensión', datos_telefono['Extension'])
    registro = interfono.add_variable(addspace, 'Registro', datos_telefono['Registro'])
    estado = interfono.add_variable(addspace, 'Estado', datos_telefono['Estado'])
    llamada = interfono.add_variable(addspace, 'Llamada', datos_telefono['Llamada'])
    



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

    print('Entro a la funcion')
    
    for lineas in lista_lineas:
        
        print('Entro bucle lineas')
        print(lineas)

        if lineas == datos_telefono['Linea']:
            print('Encontrado')
            break
            
        else:
            print('Entro else')
            lista_lineas.append(datos_telefono['Linea'])
            print(lista_lineas)
            creacion_de_parametros(datos_linea)
            break
            



if __name__ == '__main__':

    #PAREMETROS
    lista_lineas = ['LINEA'] 
    
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
    
    print('TRUE')
    print(lista_lineas)
    conexion, addr = mi_socket.accept()
    data = conexion.recv(1024)
    datos_telefono = data.decode()
    datos_telefono = json.loads(data) 
    comprobacion(datos_telefono, lista_lineas)



    #obtencion_de_paramentros(datos_telefono)
    #print('OPC ENCENDIDO')
    #message = ("Datos recibido").encode()
    #conexion.sendall(message)
    conexion.close()
