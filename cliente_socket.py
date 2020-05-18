import socket
import json

HOST = 'localhost'
PORT = 8000

my_dict = {'Extension': '9000', 'Interfono': 'SEP00505629E136', 'Estacion': 'Prueba', 'Registro': False, 'id': 'SEP00505629E136', 'Llamada': 'NO CONECTADO', 'Linea': 'L01', 'Estado': 'REPOSO'}
jsn = json.dumps(my_dict)
print(jsn)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall((jsn).encode())
    data = s.recv(1024)
    print(data)