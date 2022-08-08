import socket
import threading
import icd

class TCPClient:
    def __init__(this, IP, PORT):
        this.IP = IP #s.gethostbyname(s.gethostname())
        this.PORT = PORT
        this.ADDRESS = (IP, PORT)        
        this.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMessageToServer(this, clientMessage):
        clientEncodedMessage = clientMessage.encode("utf-8")
        if icd.isVerified(clientEncodedMessage):
            clientEncodedMessage = icd.icdParse(clientEncodedMessage)
            this.client.send(clientEncodedMessage)
        else:
            ERROR_MESSAGE_COUNT += 1

    def startConnectionToServer(this):
        this.client.connect(this.ADDRESS)
        print("Client ready to send message to server.(Enter EXIT to disconnect client)")
        while True:
            messageToServer = input("Enter message: ")
            if messageToServer.upper() == "EXIT":
                break
            this.sendMessageToServer(messageToServer)

SUCCESSFUL_MESSAGE_COUNT = 0
ERROR_MESSAGE_COUNT = 0

IP = socket.gethostbyname(socket.gethostname())
print(IP)
PORT = 9999
ADDRESS = (IP, PORT)

MESSAGE_LENGTH = 64

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

def processClientMessage(conn, addr):
    global SUCCESSFUL_MESSAGE_COUNT 
    global ERROR_MESSAGE_COUNT 
    print(f"New connection from: {addr}")
    connected = True
    while connected:
        try:
            messageContent = conn.recv(MESSAGE_LENGTH).decode("utf-8")
            if messageContent:
                print(f"Message content: {messageContent}")
                
            else:
                print("Message content is empty..")
            
            connected = False
            SUCCESSFUL_MESSAGE_COUNT +=1
        except Exception as e: 
            ERROR_EMSSAGE_COUNT += 1 
            print(f"Str:  {str(e)}")
    conn.close()  





#server hangi dosyada başlatılacak?
