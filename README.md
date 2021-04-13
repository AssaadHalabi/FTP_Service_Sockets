# FTP_Service_Sockets
A command line tool simulating the File Transfer Protocol.

## Supported commands
- put <filename>: puts the desired file in the server directory, note that any existing file with the same name is overwritten.  
- get <filename>: gets the desired file from the server directory.
- change <oldfilename> <newfilename>: changes the name of the desired file to the specified new name.
- help: Displays the valid commands supported by the server
- bye: terminates the current session.

## How to run it:
1. First run the server as in: py server.py 4118 1
2. Then run the client as in: py client.py 127.0.0.1 4118 1
3. Try all the commands, (file names preferably shouldn't contain spaces), (the server notifies if a file has been overwritten)
4. I recommend keeping DEBUG_MODE(the last command line parameter to both server.py and client.py) to 1 as it gives more insight of the current state.


## Requirements:

Having Python installed on your machine.

Link to install Python: https://www.python.org/downloads/
