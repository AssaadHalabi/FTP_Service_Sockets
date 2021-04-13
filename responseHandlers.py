# Assaad El Halabi, 201907829, ClientSide Handlers for get(tidying up the buffer unpacking) and help(parsing commands) responses at the client . I am the sole creator of this beautiful project


def handle_get_response(responseBuffer):
    name_length = responseBuffer[0] & 0b00011111
    received_file_name = (responseBuffer[1:name_length+1]).decode()
    filesize = (responseBuffer[name_length+1] << 24) & 0xff000000
    filesize += (responseBuffer[name_length+2] << 16) & 0xff0000
    filesize += (responseBuffer[name_length+3] << 8) & 0xff00
    filesize += (responseBuffer[name_length+4]) & 0xff
    file = responseBuffer[name_length+5:name_length + 6 + filesize]
    try:
        with open(received_file_name, 'wb+') as f:
            f.write(file)
    except:
        print(f"Error in saving downloaded file {received_file_name}")


def handle_help_response(responseBuffer):
    length = responseBuffer[0] & 0b00011111
    commands = list(responseBuffer[1:length+1])
    lookup = { 0:'put', 1:'get', 2:'change', 3:'help'}
    commands = list(map(lambda x: lookup[x], commands))
    print(f'Available commands: {commands}')