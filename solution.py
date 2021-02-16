#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a server socket
    serverSocket.bind(('localhost', port)) 
    serverSocket.listen(1)
    
    while True:
        #Establish the connection
        print('Ready to serve...')
        #Fill in start Fill in end
        connectionSocket, addr = serverSocket.accept() 
        try:
            message = connectionSocket.recv(1024).decode() 
            filename = message.split()[1]
            f = open(filename[1:])
            #Fill in start, fill in end
            outputdata = f.read() 
            f.close()
            #Send one HTTP header line into socket
            connectionSocket.send(bytes('HTTP/1.0 200 OK\r\n\r\n', 'UTF-8'))

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            connectionSocket.send(bytes('HTTP/1.1 404 File Not Found\nContent-Type: text/html\n\n', 'UTF-8'))
            #Close client socket
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
   webServer(13331)