# External modules
from logfunc import log, INFO, DEBUG, WARNING, ERROR # A compiled python module

# Inbuilt modules
import hashlib
import sys
import os
import time
import json_util
import socket
import threading

SERVER_PORT = 2612
IP = socket.gethostbyname(socket.gethostname())
MAX_CONNECTIONS = 25

log('File server is starting', INFO)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, SERVER_PORT))
server.listen(MAX_CONNECTIONS)

log('Server-IP: %s' % IP, DEBUG)
log('Server-PORT: %s' % SERVER_PORT, DEBUG)

running = True

while running:
    ack, addr = server.accept()
    print('Connection from: %s' % addr)