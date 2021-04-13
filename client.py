# Assaad El Halabi, 201907829, Client representing the user interface and input. I am the sole creator of this beautiful project

from responseHandlers import handle_get_response, handle_help_response
from constants import SUCCESSFUL_CHANGE_TEMPLATE, SUCCESSFUL_GET_TEMPLATE, SUCCESSFUL_PUT_TEMPLATE
from dispatchers import send_request
from socket import *
import sys
import os

_, serverName, serverPort, DEBUG_MODE = sys.argv
DEBUG_MODE = int(DEBUG_MODE)
serverPort = int(serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    command = input("$")
    command = command.strip().split()
    operation = command[0]
    filename = command[1] if len(command) >= 2 else None
    new_filename = command[2] if len(command) == 3 else None
    operation = operation.lower()
    if operation == "bye":
        print("Session is terminated.") if DEBUG_MODE else 0
        break
    send_request(clientSocket, operation, filename, new_filename, DEBUG_MODE)
    response = clientSocket.recv(2048)
    response_code = (response[0] & 0b11100000) >> 5
    if(response_code == 1):
        handle_get_response(response)
    elif(response_code == 0b110):
        handle_help_response(response)
    
    if(DEBUG_MODE):
        print(SUCCESSFUL_PUT_TEMPLATE.substitute(filename=filename)) if (response_code == 0 and operation == "put") else 0
        print(SUCCESSFUL_CHANGE_TEMPLATE.substitute(filename=filename, new_filename=new_filename)) if (response_code == 0 and operation == "change") else 0
        print(SUCCESSFUL_GET_TEMPLATE.substitute(filename=filename)) if (response_code == 1) else 0
        print("A change error occurred") if (response_code == 0b101) else 0
        print("Error-File Not Found") if (response_code == 0b010) else 0
        print('Unknown command, type "help" for available commands ') if (response_code == 0b011) else 0

clientSocket.close()



