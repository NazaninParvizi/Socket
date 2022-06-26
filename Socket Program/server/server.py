import socket
import os

#serverPort = 8500
#BufferSIZE = 1024

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8500))
server.listen() 
print("Server is up!")

while True:
    conn, addr = server.accept()
    print(f'NEW CLIENT {addr} connected')

    #file name received from client
    creq = conn.recv(1024)  
    handler_client = creq.decode("utf-8").lower()
    if handler_client == 'put':
        creq = conn.recv(1024)
        file_name = creq.decode("utf-8")
        f = open(file_name, "wb")
        print('file uploaded')
        data = conn.recv(1024)
        while(data):
            f.write(data)
            data = conn.recv(1024)
        #write received data
        f.close()    
        print('Upload completed')
        
    elif handler_client == 'get':
        creq = conn.recv(1024)        
        file_name = creq.decode("utf-8")
        f = open(file_name, "rb")
        print('Downloading...')
        data = f.read(1024)
        while(data):
            conn.send(data)
            data = f.read(1024)
        f.close()
        print('Download completed')

    elif handler_client == 'ls':
        conn.send("._.".join(os.listdir()).encode('utf-8'))   #send list files to client

    elif handler_client == 'done' and handler_client == "":
        pass


    conn.close()