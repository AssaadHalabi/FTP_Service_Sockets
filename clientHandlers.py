# Assaad El Halabi, 201907829, ClientSide Handlers implementations. I am the sole creator of this beautiful project
from bufferCreation import create_success_change_client_buffer, create_get_client_buffer
import os


def put(clientSocket, filename: str, *args, **kwargs):
    with open(filename, 'rb') as file:
        name_length = len(filename)
        file_size = os.path.getsize(filename)
        data = file.read()
        buffer = bytearray()
        if(name_length > 30):
            print("File name can not exceed 30 characters, please try again.")
            return
        buffer.append(0b000 & 0b111)
        buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
        buffer[len(buffer) -1] = buffer[len(buffer) -1] | (name_length & 0b11111)
        buffer.extend(filename.encode())
        buffer.append((file_size & 0xff000000) >> 24)
        buffer.append((file_size & 0xff0000) >> 16)
        buffer.append((file_size & 0xff00) >> 8)
        buffer.append((file_size & 0xff))
        buffer.extend(data)
        clientSocket.send(buffer)
        return
        
def get(clientSocket, filename: str, *args, **kwargs):
    name_length = len(filename)
    buffer = create_get_client_buffer(filename, name_length)
    clientSocket.send(buffer)
    return

def change(clientSocket, filename, new_filename, *args, **kwargs):
    name_length = len(filename)
    new_length = len(new_filename)
    buffer = create_success_change_client_buffer(filename, name_length, new_filename, new_length)
    clientSocket.send(buffer)
    return

def help(clientSocket, *args, **kwargs):
    buffer = bytearray()
    buffer.append((0b011 & 0b111))
    buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
    clientSocket.send(buffer)
    return

def unknown(clientSocket, *args, **kwargs):
    buffer = bytearray()
    buffer.append((0b111 & 0b111))
    buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
    clientSocket.send(buffer)