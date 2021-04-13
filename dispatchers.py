# Assaad El Halabi, 201907829, High level clientSide and serverSide dispatchers that provide custom data and dispatch a specific method based on requested operation. I am the sole creator of this beautiful project

from serverHandlers import change, get, put, unknown, help
from lookupTable import CLIENT_HANDLERS

#Client-side
def send_request(clientSocket, operation, filename: str, new_filename: str, DEBUG_MODE):
    if(not operation):
        print('Please enter a command, type "help" for available commands')
    availableCommands = set(CLIENT_HANDLERS.keys())
    operation = operation if operation in availableCommands else 'unknown'
    requestMethod = CLIENT_HANDLERS.get(operation)
    requestMethod(clientSocket, filename, new_filename, DEBUG_MODE)


#ServerSide
def invoke_operation_handler(connectionSocket, buffer, opcode, DEBUG_MODE):
    print(f'opcode: {opcode}') if DEBUG_MODE else 0
    if(opcode == 0):
        name_length = buffer[0] & 0b00011111
        filename = (buffer[1:name_length+1]).decode()
        filesize = (buffer[name_length+1] << 24) & 0xff000000
        filesize += (buffer[name_length+2] << 16) & 0xff0000
        filesize += (buffer[name_length+3] << 8) & 0xff00
        filesize += (buffer[name_length+4]) & 0xff
        file = buffer[name_length+5:name_length + 6 + filesize]
        put(connectionSocket, filename, file, DEBUG_MODE)
    elif(opcode == 1):
        name_length = buffer[0] & 0b00011111
        filename = (buffer[1:name_length+1]).decode()
        get(connectionSocket, filename, DEBUG_MODE)
    elif(opcode == 2):
        name_length = buffer[0] & 0b00011111
        filename = (buffer[1:name_length+1]).decode()
        new_length = buffer[name_length+1]
        new_filename = (buffer[len(buffer) - new_length:len(buffer)]).decode()
        change(connectionSocket, filename, new_filename, DEBUG_MODE)

    elif(opcode == 0b111):
        unknown(connectionSocket)

    elif(opcode == 0b011):
        actions = [0,1,2,3]
        length = len(actions)
        commands = bytes(actions)
        help(connectionSocket, length, commands)