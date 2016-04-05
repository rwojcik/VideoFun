#!/usr/bin/env python

import socket
from UserString import MutableString
import cv2
import numpy as np

class FrameEditor:
    def frame_edit(self, frame):
        cv2.ellipse(frame,(256,256),(100,50),0,0,180,255,-1)
        return frame

class FrameSinkShower:
    def frame_sink(self, frame):
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

def recive_and_sink_video(ip, port, frameEditor, frameSink):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    while 1:
        s.send('o')
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

        frame = cv2.imdecode(np.fromstring(str(frame_data), dtype=np.uint8), 1)
        frame = frameEditor.frame_edit(frame)
        if not frameSink.frame_sink(frame):
            break
    s.close()

recive_and_sink_video(TCP_IP, TCP_PORT, FrameEditor(), FrameSinkShower())