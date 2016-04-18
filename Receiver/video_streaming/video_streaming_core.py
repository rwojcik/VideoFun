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

def recv_data(number, s):
    frame_data = MutableString()
    while number > 0:
        read = s.recv(number)
        frame_data += read
        number -= len(read)
    return frame_data


def readNumber(s):
    ch = s.recv(1)
    number = ""
    while ch.isdigit():
        number += ch
        ch = s.recv(1)
    number = int(number)
    return number

class FrameGenearator:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def generator_init(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip, self.port))

    def gen_frame(self):
        self.s.send('o')
        number = readNumber(self.s)
        frame_data = recv_data(number, self.s)
        print "read frame in generator"
        print len(frame_data)
        frame = cv2.imdecode(np.fromstring(str(frame_data), dtype=np.uint8), 1)
        return frame

    def generator_finish(self):
        self.s.close()

class CameraFrameGenearator:

    def generator_init(self):
        self.camera = cv2.VideoCapture(0)

    def gen_frame(self):
        f,frame = self.camera.read()
        return frame

    def generator_finish(self):
        return

def recive_and_sink_video(frameEditor, framesDst, framesSrc):
    framesSrc.generator_init()
    framesDst.sink_init()
    while 1:
        frame = framesSrc.gen_frame()
        frame = frameEditor.frame_edit(frame)
        if not framesDst.frame_sink(frame):
            break
    framesDst.sink_finish()
    framesSrc.generator_finish()