#TCP socket, client, example 2
#this client connects to the server given with the IP and Port# below and sends a message to server
from socket import *

serverName="160.75.192.133"
serverPort=12000

clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))


i=0
while i<6:

    modifiedMessage=clientSocket.recv(1024)
    print(modifiedMessage.decode("utf-8"))
    if modifiedMessage.decode("utf-8")=="User is not registered!":
        clientSocket.close()
        exit(0)

    message = input()
    clientSocket.send(message.encode())
    
    
    i+=1  

fs=clientSocket.recv(1024)
print("Your final score is: ",fs.decode())
clientSocket.close()
exit(0)
       

