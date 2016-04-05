#!/usr/bin/env python

import socket
from UserString import MutableString
import cv2
import numpy as np

class FrameEditorEmpty:
    def frame_edit(self, frame):
        #cv2.ellipse(frame,(256,256),(100,50),0,0,180,255,-1)
        return frame

class FrameEditorEllipse:
    def frame_edit(self, frame):
        cv2.ellipse(frame,(256,256),(100,50),0,0,180,255,-1)
        return frame


class FrameSinkShower:
    def frame_sink(self, frame):
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True

    def sink_init(self):
        return

    def sink_finish(self):
        return

class FrameSinkServer:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def sink_init(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, self.port))
        s.listen(1)
        self.conn, self.addr = s.accept()

    def sink_finish(self):
        self.conn.close()

    def frame_sink(self, frame):
        retval, buf = cv2.imencode(".jpg", frame)
        if not retval:
            return False
        self.conn.send("%d*" % (buf.size))
        self.conn.send(buf)
        return True

def recive_and_sink_video(ip, port, frameEditor, frameSink):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    frameSink.sink_init()
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
    frameSink.sink_finish()
    s.close()