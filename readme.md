#Simple Plain-Text Reverse Shell

##Overview
This is a rudimentary reverse shell service implemented in python over TCP sockets for academic purposes.
The commands it can execute are very limited compared to a full fledged shell.
It is meant for simple undetected execution of commands on the remote system.
The client is robust and will survive a variety of failures and attempt to reconnect as soon as it can.

##How to Use
* Replace the IP address in the client file to an expected server ip address
* Place the client.py file on the target machine and execute it in the background
* Start the server.py file on the host whose IP matches the one in the client.py file
* Enter commands as directed


##Circumventing some of the Limitations
One way to go around the limitations of not even being able to change directories is to script the sequence of commands to be executed in a .sh file on the target machine using the reverse shell.
Then simply execute the script using '/bin/bash scriptsh'. The results should be sent back to you.

