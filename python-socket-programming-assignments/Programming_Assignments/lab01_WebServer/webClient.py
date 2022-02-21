from http import client, server
from socket import *
hostName = input('Input Host Name:')
serverPort = int(input('Input Server Port:'))
fileNmae = input('Input File Name:')
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((hostName, serverPort))
clientSocket.sendall("GET /{} HTTP/1.1\r\n".format(fileNmae).encode())
clientSocket.send("\r\n".encode())
while True:
    message = clientSocket.recv(1024).decode()
    if len(message) == 0:
        break
    print(message)
clientSocket.close()