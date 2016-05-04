#!/usr/bin/env python

import socket
from UserString import MutableString
import cv2
import numpy as np
import threading, time
from msvcrt import getch

key = ''

class FrameEditorEmpty:
    def frame_edit(self, frame):
        return frame

class FrameEditorEllipse:
    def frame_edit(self, frame):
        cv2.ellipse(frame,(256,256),(100,50),0,0,180,255,-1)
        return frame

class FrameEditorGreyscale:
    def frame_edit(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame

class FrameEditorSmoothing:
    def frame_edit(self, frame):
        frame = cv2.GaussianBlur(frame, (11, 11), 0)
        return frame

class FrameEditorDerivative:
    def frame_edit(self, frame):
        frame = cv2.Laplacian(frame, cv2.CV_64F)
        return frame

class FrameEditorCircles:
    def frame_edit(self, frame):
        gsFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gsFrame, cv2.HOUGH_GRADIENT, dp=2, minDist=50, param1=100, param2=60, minRadius=50, maxRadius=0)
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img=frame,center=(i[0],i[1]),radius=i[2],color=(128,128,128,128),thickness=1)
            cv2.circle(img=frame,center=(i[0],i[1]),radius=2,color=(64,64,64,128),thickness=1)
        return frame


class FrameSinkShower:
    def frame_sink(self, frame):
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            key = 'q'
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
        try:
            retval, buf = cv2.imencode(".jpg", frame)
            if not retval:
                return False
            self.conn.send("%d*" % (buf.size))
            self.conn.send(buf)
        except (socket.error, cv2.error) as e:
            print str(e)
            return False
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
    threading.Thread(target = key_reader).start()
    while 1:
        framesSrc.generator_init()
        framesDst.sink_init()
        while 1:
            frame = framesSrc.gen_frame()
            frame = frameEditor.frame_edit(frame)
            if not framesDst.frame_sink(frame) or key == 'q':
                break
        framesDst.sink_finish()
        framesSrc.generator_finish()
        if key == 'q':
            break

def key_reader():
    global key
    lock = threading.Lock()
    while True:
        with lock:
            key = getch()
        if key == 'q':
            break