# Assaad El Halabi, 201907829, Handler implementations dispatched according to operation by dispatcher. I am the sole creator of this beautiful project


from bufferCreation import create_get_server_buffer
from constants import FILEDIR
import os


def send_successful_put_and_change_response(connectionSocket, overwrite=False):
    buffer = bytearray()
    buffer.append(0)
    print("File has been overwritten successfully, (put with same name as another file existing in server directory)") if overwrite else 0
    connectionSocket.send(buffer)
    return


def put(connectionSocket, filename: str, file, DEBUG_MODE):
    try:
        path = os.path.join(FILEDIR, filename)
        overwrite = os.path.exists(path)
        with open(path, 'wb+') as f:
            f.write(file)
        send_successful_put_and_change_response(connectionSocket, overwrite)
    except:
        print("Put error") if DEBUG_MODE else 0
    return

def get(connectionSocket, filename: str, DEBUG_MODE):
    path = os.path.join(FILEDIR, filename)
    if(not os.path.exists(path)):
        buffer = bytearray()
        buffer.append(0b010 & 0b111)
        buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
        connectionSocket.send(buffer)
        return
    try:
        with open(path , 'rb') as f:
            file = f.read()
            name_length = len(filename)
            file_size = os.path.getsize(path)
            buffer = create_get_server_buffer(filename, file_size, name_length, file)
            connectionSocket.send(buffer)
    except:
        print("Get error") if DEBUG_MODE else 0
    return


def change(connectionSocket, filename: str, new_filename: str, DEBUG_MODE):
    try:
        os.rename(os.path.join(FILEDIR, filename), os.path.join(FILEDIR, new_filename))
        send_successful_put_and_change_response(connectionSocket)
    except:
        print("Change error") if DEBUG_MODE else 0
        buffer = bytearray()
        buffer.append((0b101 & 0b111))
        buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
        connectionSocket.send(buffer)
    return
    
def unknown(connectionSocket):
    buffer = bytearray()
    buffer.append((0b011 & 0b111))
    buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
    connectionSocket.send(buffer)

def help(connectionSocket, length: int, commands):
    buffer = bytearray()
    buffer.append((0b110 & 0b111))
    buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
    buffer[len(buffer) -1] = buffer[len(buffer) -1] | (length & 0b11111)
    buffer.extend(commands)
    connectionSocket.send(buffer)

