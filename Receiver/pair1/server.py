#!/usr/bin/env python

import socket
import cv2


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr

camera = cv2.VideoCapture(0)

while 1:
    if not conn.recv(1):
        break
    f,img = camera.read()
    cv2.circle(img,(447,63), 63, (0,0,255), -1)
    retval, buf = cv2.imencode(".jpg", img)
    if not retval:
        print "retval false"
        continue
    print "Sending %d data " % buf.size
    conn.send("%d*" % (buf.size))
    conn.send(buf)
    print "Send %d data " % buf.size

conn.close()