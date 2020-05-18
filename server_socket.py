import socket
import json
from opcua.crypto import uacrypto
from opcua import Server, ua
import time


def creacion_desde_linea(datos_telefono):
    
    linea = node.add_object(addspace, datos_telefono['Linea'])
    estacion = linea.add_object(addspace, datos_telefono['Estacion'])
    interfono = estacion.add_object(addspace, datos_telefono['Interfono'])
    id_telefono = interfono.add_variable(addspace, 'Id', datos_telefono['id'])
    extension = interfono.add_variable(addspace, 'Extensión', datos_telefono['Extension'])
    registro = interfono.add_variable(addspace, 'Registro', datos_telefono['Registro'])
    estado = interfono.add_variable(addspace, 'Estado', datos_telefono['Estado'])
    llamada = interfono.add_variable(addspace, 'Llamada', datos_telefono['Llamada'])

    dic_lineas[datos_telefono['Linea']] = linea
    print(dic_lineas)


def creacion_desde_estacion(datos_linea):

    linea = dic_lineas[datos_telefono['Linea']]
    estacion = linea.add_object(addspace, datos_telefono['Estacion'])
    interfono = estacion.add_object(addspace, datos_telefono['Interfono'])
    id_telefono = interfono.add_variable(addspace, 'Id', datos_telefono['id'])
    extension = interfono.add_variable(addspace, 'Extensión', datos_telefono['Extension'])
    registro = interfono.add_variable(addspace, 'Registro', datos_telefono['Registro'])
    estado = interfono.add_variable(addspace, 'Estado', datos_telefono['Estado'])
    llamada = interfono.add_variable(addspace, 'Llamada', datos_telefono['Llamada'])

    dic_estaciones[datos_telefono['Estacion']] = estacion
    print(dic_estaciones)
    
def creacion_desde_interfono(datos_linea):
    
    estacion = dic_estaciones[datos_telefono['Estacion']]
    interfono = estacion.add_object(addspace, datos_telefono['Interfono'])
    id_telefono = interfono.add_variable(addspace, 'Id', datos_telefono['id'])
    extension = interfono.add_variable(addspace, 'Extensión', datos_telefono['Extension'])
    registro = interfono.add_variable(addspace, 'Registro', datos_telefono['Registro'])
    estado = interfono.add_variable(addspace, 'Estado', datos_telefono['Estado'])
    llamada = interfono.add_variable(addspace, 'Llamada', datos_telefono['Llamada'])

    dic_interfonos[datos_telefono['Interfono']] = interfono
    print(dic_interfonos)

def cambio_de_variables(datos_liena):

    interfono = dic_interfonos[datos_telefono['Interfono']]
    id_telefono = interfono.add_variable(addspace, 'Id', datos_telefono['id'])
    extension = interfono.add_variable(addspace, 'Extensión', datos_telefono['Extension'])
    registro = interfono.add_variable(addspace, 'Registro', datos_telefono['Registro'])
    estado = interfono.add_variable(addspace, 'Estado', datos_telefono['Estado'])
    llamada = interfono.add_variable(addspace, 'Llamada', datos_telefono['Llamada'])

    id_telefono.set_writable()
    extension.set_writable()
    registro.set_writable()
    estado.set_writable()
    llamada.set_writable()

    id_telefono.set_value(datos_telefono['id'])
    extension.set_value(datos_telefono['Extension'])
    registro.set_value(datos_telefono['Registro'])
    estado.set_value(datos_telefono['Estado'])
    llamada.set_value(datos_telefono['Llamada'])

def comprobacion(datos_telefono, lista_lineas, lista_estacion, lista_interfono):

    print('Entro a la funcion')
    
    
    if datos_telefono['Linea'] not in lista_lineas:
        print('Linea no Encontrada')
        lista_lineas.append(datos_telefono['Linea'])
        lista_estacion.append(datos_telefono['Estacion'])
        lista_interfono.append(datos_telefono['Interfono'])
        creacion_desde_linea(datos_telefono)
       
    else:
        print('Linea encontrado')
        if datos_telefono['Estacion'] not in lista_estacion:
            print('Estacion no encontrada')
            lista_estacion.append(datos_telefono['Estacion'])
            creacion_desde_estacion(datos_telefono)
        else:
            print('Estacion Encontrada')
            if datos_telefono['Interfono'] not in lista_interfono:
                print('Interfono no encontrado')
                lista_interfono.append(datos_telefono['Interfono'])
                creacion_desde_interfono(datos_telefono)
            else:
                print('Interfono encontrado')
                cambio_de_variables(datos_telefono)

                
                
if __name__ == '__main__':

    #PAREMETROS
    lista_lineas = []
    lista_estacion = []
    lista_interfono = []
    global dic_lineas, dic_estaciones, dic_interfonos
    dic_lineas = {}
    dic_estaciones = {}
    dic_interfonos = {}

    
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
    print(lista_estacion)
    print(lista_interfono)
    conexion, addr = mi_socket.accept()
    data = conexion.recv(1024)
    datos_telefono = data.decode()
    datos_telefono = json.loads(data) 
    comprobacion(datos_telefono, lista_lineas, lista_estacion, lista_interfono)



    #obtencion_de_paramentros(datos_telefono)
    #print('OPC ENCENDIDO')
    #message = ("Datos recibido").encode()
    #conexion.sendall(message)
    conexion.close()
