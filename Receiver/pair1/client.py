#!/usr/bin/env python

import socket
from UserString import MutableString
import cv2
import numpy as np


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)
while 1:
    ch = s.recv(1)
    print "first ch = %s" % ch
    number = ""
    while ch.isdigit():
        number += ch
        ch = s.recv(1)
        print "now number is %s" % number
    number = int(number)
    frame_data = MutableString()
    while number > 0:
        read = s.recv(number)
        frame_data += read
        number -= len(read)
    print "read frame"
    print len(frame_data)

    frame = cv2.imdecode(np.fromstring(str(frame_data), dtype=np.uint8), 0)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

s.close()