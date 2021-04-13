# FTP_Service_Sockets
A command line tool simulating the File Transfer Protocol.

## Supported commands
- put <filename>: puts the desired file in the server directory, note that any existing file with the same name is overwritten.  
- get <filename>: gets the desired file from the server directory.
- change <oldfilename> <newfilename>: changes the name of the desired file to the specified new name.
- help: Displays the valid commands supported by the server
- bye: terminates the current session.
