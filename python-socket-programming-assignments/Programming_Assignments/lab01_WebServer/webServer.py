from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 12000
host = 'localhost'
serverSocket.bind((host, serverPort))
serverSocket.listen(5)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end 
    try:
        message = connectionSocket.recv(1024).decode() #Fill in start #Fill in end 
        filename = message.split()[1]
        with open(filename[1:]) as f:
            outputdata = f.read() #Fill in start #Fill in end 
        #Send one HTTP header line into socket
        connectionSocket.sendall("HTTP/1.1 200 ok\r\n".encode())
        connectionSocket.send("\r\n".encode())
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
    except IOError:
        #Send response message for file not found
        connectionSocket.sendall("HTTP/1.1 404 not found\r\n".encode())
        connectionSocket.send("\r\n".encode())
        #Close client socket
    except:
        connectionSocket.sendall("HTTP/1.1 500 internal server error\r\n".encode())
        connectionSocket.send("\r\n".encode())
    finally:
        connectionSocket.close()
    
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data