import socket
import json

#HOST = 'localhost'
#PORT = 8000


#with socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) as s:
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.bind((HOST, PORT))
#    s.listen(1)
#    conn, addr = s.accept()

mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000))
mi_socket.listen(5)


    #with conn:
    #while True:
    #    data = conn.recv(1024)
    #    new_data = data.decode()
    #    new_data = json.loads(data)
    #    print(new_data["Name"],"has connected from",addr)
    #    print(new_data["age"])
            #message = ("Hello %s welcome to the chat server" % new_data["Name"]).encode()
            #conn.sendall(message)
            #if not data:
            #    conn.sendall(data)
        #conn.close()

while True:
    conexion, addr = mi_socket.accept()
    data = conexion.recv(1024)
    new_data = data.decode()
    new_data = json.loads(data)
    print(new_data)
    print(new_data["Name"],"has connected from",addr)
    print(new_data["age"])
    message = ("Datos recibido").encode()
    conexion.sendall(message)
    conexion.close()
