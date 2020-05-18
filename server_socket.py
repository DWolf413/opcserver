import socket
import json
from opcua.crypto import uacrypto
from opcua import Server, ua
import time


def creacion_desde_linea(datos_telefono):
    
    global dic_lineas = {}
    linea = node.add_object(addspace, datos_telefono['Linea'])
    estacion = linea.add_object(addspace, datos_telefono['Estacion'])
    interfono = estacion.add_object(addspace, datos_telefono['Interfono'])
    id_telefono = interfono.add_variable(addspace, 'Id', datos_telefono['id'])
    extension = interfono.add_variable(addspace, 'Extensión', datos_telefono['Extension'])
    registro = interfono.add_variable(addspace, 'Registro', datos_telefono['Registro'])
    estado = interfono.add_variable(addspace, 'Estado', datos_telefono['Estado'])
    llamada = interfono.add_variable(addspace, 'Llamada', datos_telefono['Llamada'])

    lista_nodo_linea = [linea]
    print(lista_nodo_linea)

    dic_lineas[datos_telefono['Linea']] = linea


def creacion_desde_estacion(datos_linea, linea):

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

def comprobacion(datos_telefono, lista_lineas, lista_estacion):

    print('Entro a la funcion')
    print(lista_lineas)
    
    if datos_telefono['Linea'] not in lista_lineas:
        print('No Encontrado1')
        lista_lineas.append(datos_telefono['Linea'])
        creacion_desde_linea(datos_telefono)
       
    else:
        print('Encontrado')
        if datos_telefono['Estacion'] not in lista_estacion:
            print('Estacion no encontrada')
            lista_estacion.append(datos_telefono['Estacion'])
            #creacion_desde_estacion(datos_telefono, linea)
        else:
            print('Encontrado') 

           



if __name__ == '__main__':

    #PAREMETROS
    lista_lineas = []
    lista_estacion = []

    
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
    comprobacion(datos_telefono, lista_lineas, lista_estacion)



    #obtencion_de_paramentros(datos_telefono)
    #print('OPC ENCENDIDO')
    #message = ("Datos recibido").encode()
    #conexion.sendall(message)
    conexion.close()
