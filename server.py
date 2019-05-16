#TCP socket, threaded server, example 2
#this server receives a message from client and print it on screen, then wait for another connection requests as well as listen for connected clients

from socket import *
import threading

registeredusers = ['ece','123']
questions = ['1)Which of the following statement is false about transportation layer? <br/>  A)In UDP IP datagrams with same destination port number but different source IP address will be directed to different socket at destination <br/>  B)TCP is a reliable protocol <br/>  C) Network layer build on transport layer  <br/>  D)Network layer provides logical communication between hosts <br/> ',
'2)Which application can tolerate data loss but their required minimum amount of throughput is elastic? <br/>  A)Skype Call <br/>  B)Gmail <br/>  C)Syllabus <br/>  D)SMS <br/> ',
'3)Which of the following is true about e-mail? <br/>  A)User mailboxes kept in user agents. <br/>  B)User agent and mail server communicate through STMP protocol. <br/>  C)Two user agent can directly communicate with each other. <br/>  D)In e-mail, there is a three phases of transfer: handshaking, transfer of message and closure. <br/> ',
'4)Imagine a 48 bit length packet with link bandwidth 0.6bps. Length of the physical link between two router is 175m. If propagation speed is 35m/s, and processing delay and queue delay is ignored; find the time that passes until this packet transfer from one router to another. <br/>  A)83s <br/>  B)75s <br/>  C)85s <br/>  D)105s <br/> ',
'5)Which of the following is a TCP service? <br/>  A)ARP <br/>  B)Congestion Control <br/>  C)Error Avoidance <br/>  D)Acknowlegement <br/> ']

rights = ['a','b','d','c','b']


class ThreadedServer():

    def getusername(self,client,addr):
        client.send("Please enter your username:".encode())
        recvuser = client.recv(1024).decode("utf-8")
        flag = False
        for user in registeredusers:
            if user == recvuser:
                flag = True
        if flag:
            print("succesfull entry")
            threading.Thread(target = self.sendQuestion,args = (client,addr)).start()
        else:
            client.send("User is not registered!".encode())
            print (addr , " made a unsuccessful login!")
            client.close()                        
            exit(0)


    def sendQuestion(self, client, addr):
        
        clientanswers = []
        for quest in questions:
            client.send(quest.encode())
            returned = client.recv(1024)
            answer = returned.decode("utf-8")
            clientanswers.append(answer.lower())

        fs=0
        i=0
        while i<5:
            if clientanswers[i] == rights[i]:
                fs +=5
            i+=1

        print(addr, " final score is: ", fs)
        client.send(str(fs).encode())
        print (addr , " is closed")
        client.close()                        
        exit(0)
        

    def __init__(self,serverPort):

        try:
            serverSocket=socket(AF_INET,SOCK_STREAM)

        except:
    
            print ("Socket cannot be created!!!")
            exit(1)
            
        print ("Socket is created...")

        try:
            serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
    
            print ("Socket cannot be used!!!")
            exit(1)

        print ("Socket is being used...")

        try:
            serverSocket.bind(('',serverPort))
        except:
        
            print ("Binding cannot de done!!!")
            exit(1)

        print ("Binding is done...")

        try:
            serverSocket.listen(45)
        except:
    
            print ("Server cannot listen!!!")
            exit(1)

        print ("The server is ready to receive")


        while True:
            connectionSocket,addr=serverSocket.accept()
            threading.Thread(target=self.getusername,args=(connectionSocket,addr)).start()
            

if __name__=="__main__":
    serverPort=12000
    ThreadedServer(serverPort)
	
#multithreaded client is threaded too no need to wait for each other
#threaded only server side not client they wait each other