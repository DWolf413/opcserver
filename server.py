#import sys
#from opcua.crypto import uacrypto
#from opcua import Server, ua
#from random import randint
#import datetime
#import time


#sys.path.insert(0, "..")


#server.set_security_policy([ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])
# load server certificate and private key. This enables endpoints
# with signing and encryption.
#server.load_certificate("/home/administrador/opc/opcserver/my_cert.der")
#server.load_private_key("/home/administrador/opc/opcserver/my_private_key.pem")


#if __name__ == '__main__':
    #server = Server()

    #url = "opc.tcp://192.168.100.6:4840"
    #server.set_endpoint(url)

    #server.set_security_policy([ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])
    #server.load_certificate("/home/administrador/opc/opcserver/certificados/my_cert.der")
    #server.load_private_key("/home/administrador/opc/opcserver/certificados/my_private_key.pem")

    #name = "OPCUA_SERVER"
    #addspace = server.register_namespace(name)

    #node = server.get_objects_node()

    #Param = node.add_object(addspace, "Parameters")

    #Temp = Param.add_variable(addspace, "Tempreature", 0)
    #Press = Param.add_variable(addspace, "Pressure", 0)
    #Time = Param.add_variable(addspace, "Time", 0)

    #Temp.set_writable()
    #Press.set_writable()
    #Time.set_writable()

    #server.start()
    #print("Server at {}".format(url))

    while True:
        Temperature = randint(10,50)
        Pressure = randint(20, 999)
        TIME = datetime.datetime.now()

        print (Temperature, Pressure, TIME)

        Temp.set_value(Temperature)
        Press.set_value(Pressure)
        Time.set_value(TIME)

        time.sleep(2)


