__author__ = 'RiteshReddy'
import socket, os


serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(("", 9987))
serversock.listen(1)
(clientsock, addr) = serversock.accept()
print "Connection Established!"
t = raw_input("Enter Command: ")
while t != "quit()":
    clientsock.send(t)
    print clientsock.recv(1048576)
    t = raw_input("Enter Command: ")
clientsock.close()
serversock.close()

