import socket_file
import threading

def startServerListener(client_number):
    global ERROR_MESSAGE_COUNT
    server= socket_file.server
    server.listen(client_number)
    print("Server started. Waiting for clients...")
    while True:
        try:
            conn, addr = server.accept()
            messageHandleThread = threading.Thread(target=socket_file.processClientMessage,args=(conn, addr))
            messageHandleThread.start()
        except Exception as e:
            print(f"Server error: {e}")
            ERROR_MESSAGE_COUNT += 1 


if __name__ == "__main__":
    startServerListener(10)

