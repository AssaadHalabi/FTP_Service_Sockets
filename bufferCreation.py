
# Assaad El Halabi, 201907829, Facilitates Buffer Creation. I am the sole creator of this beautiful project


def create_get_client_buffer(filename: str, name_length: int):
    buffer = bytearray()
    if(name_length > 30):
        print(f"File name can not exceed 30 characters ({name_length > 30}), please try again.")
        return
    buffer.append(0b001 & 0b111)
    buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
    buffer[len(buffer) -1] = buffer[len(buffer) -1] | (name_length & 0b11111)
    buffer.extend(filename.encode())
    return buffer



def create_get_server_buffer(filename: str, file_size: int, name_length:int, file):
    buffer = bytearray()
    if(name_length > 30):
        print("File name can not exceed 30 characters, please try again.")
        return
    buffer.append(0b001 & 0b111)
    buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
    buffer[len(buffer) -1] = buffer[len(buffer) -1] | (name_length & 0b00011111)
    buffer.extend(filename.encode())
    buffer.append((file_size & 0xff000000) >> 24)
    buffer.append((file_size & 0xff0000) >> 16)
    buffer.append((file_size & 0xff00) >> 8)
    buffer.append((file_size & 0xff))
    buffer.extend(file)
    return buffer


def create_success_change_client_buffer(filename: str, name_length: int, new_filename: str, new_length: int):
    buffer = bytearray()
    if(new_length > 30):
        print(f"File name can not exceed 30 characters ({new_length > 30}), please try again.")
        return
    buffer.append(0b010 & 0b111)
    buffer[len(buffer) -1] = buffer[len(buffer) -1] << 5
    buffer[len(buffer) -1] = buffer[len(buffer) -1] | (name_length & 0b11111)
    buffer.extend(filename.encode())
    buffer.append(new_length & 0xff)
    buffer.extend(new_filename.encode())
    return buffer

