import socket

connection = True
while connection:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1',8500))

    request = input('What is your request :>').lower()
    client.send(request.encode('utf-8'))
    if request in ['get', 'put']:
        fileName = input('\nEnter the file name: ')
        client.send(fileName.encode('utf-8'))
        
    if request == 'put':
        f = open(fileName,"rb")
        print('file is Sending to server...')
        data = f.read(1024)
        while (data):
            client.send(data)
            data = f.read(1024)
        f.close()
        print('Done sending')
        
    elif request == 'get':
        f = open(fileName, "wb")
        print('Receiving file..')
        data = client.recv(1024)
        while (data):
            f.write(data)
            data = client.recv(1024)
        f.close()
        print('Done receiving file')
    
    elif request == 'ls':
        print(client.recv(1024).decode('utf-8'))

    elif request == 'done':
        print('DONE!')
        connection = False

    else:
        print("cant undertstand your request!!!")

    client.close()
