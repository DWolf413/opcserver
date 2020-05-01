from opcua import Server
from random import randint
import datetime
import time
from opc_server_security import OPC_SERVER_SECURITY

opc_server = OPC_SERVER_SECURITY()
server = Server()

url = "opc.tcp://192.168.100.6:4840"
server.set_endpoint(url)

#server.set_security_policy([ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])
# load server certificate and private key. This enables endpoints
# with signing and encryption.
#server.load_certificate("/home/administrador/opc/opcserver/my_cert.der")
#server.load_private_key("/home/administrador/opc/opcserver/my_private_key.pem")

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Tempreature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print("Server at {}".format(url))
opc_server.init_opc_server_security('192.168.100.6')
opc_server.set_server_credentials('admin', 'admin')

while True:

    res = opc_server.client_authentication()
    
    while res:
        Temperature = randint(10,50)
        Pressure = randint(20, 999)
        TIME = datetime.datetime.now()
    

    print (Temperature, Pressure, TIME)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(2)


