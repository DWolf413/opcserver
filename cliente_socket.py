import socket
import json

HOST = 'localhost'
PORT = 8000

my_dict = {"Name":"Bob", "age":39}
jsn = json.dumps(my_dict)
print(jsn)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall((jsn).encode())
    data = s.recv(1024)
    print(data)