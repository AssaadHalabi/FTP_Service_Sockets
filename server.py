# Assaad El Halabi, 201907829, Server. I am the sole creator of this beautiful project

from dispatchers import invoke_operation_handler
from socket import *
import sys
import os

serverPort = int(sys.argv[1])
DEBUG_MODE = int(sys.argv[2])
if(not os.path.exists('files')):
    os.makedirs('files')
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print ('The server is ready to receive') if DEBUG_MODE else 0
    connectionSocket, addr = serverSocket.accept()
    print ("Accepted connection from", addr) if DEBUG_MODE else 0
    while True:
        buffer = connectionSocket.recv(2048)
        print(len(buffer)) if DEBUG_MODE else 0
        if len(buffer)==0:
            break
        opcode = (buffer[0] & 0b11100000) >> 5
        invoke_operation_handler(connectionSocket, buffer, opcode, DEBUG_MODE)
    connectionSocket.close()


