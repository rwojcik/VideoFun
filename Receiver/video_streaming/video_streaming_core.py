#!/usr/bin/env python

import socket
from UserString import MutableString
import cv2
import numpy as np
import threading, time
from frame_editor import *
from frame_merge import *
from msvcrt import getch

key = ''

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
        self.ports = port.split(",")
        self.sockets_connections = list()

    def sink_init(self):
        for port in self.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.ip, port))
            s.listen(1)
            conn, addr = s.accept()
            self.sockets_connections.extend(conn)

    def sink_finish(self):
        for conn in self.sockets_connections:
            conn.close()

    def frame_sink(self, frame):
        try:
            retval, buf = cv2.imencode(".jpg", frame)
            if not retval:
                return False
            for conn in self.sockets_connections:
                conn.send("%d*" % (buf.size))
                conn.send(buf)
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

class FrameGenerator:

    def __init__(self, ip, port):
        self.ip = ip
        self.ports = port.split(",")
        self.sockets = list()

    def generator_init(self):
        for port in self.ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, self.port))
            self.sockets.extend(s)

    def gen_frame(self):
        frames = list()
        for s in self.sockets:
            s.send('o')
            number = readNumber(self.s)
            frame_data = recv_data(number, self.s)
            print "read frame in generator"
            print len(frame_data)
            frames.extend(cv2.imdecode(np.fromstring(str(frame_data), dtype=np.uint8), 1))
        return frames

    def generator_finish(self):
        for s in self.sockets:
            s.close()

class CameraFrameGenearator:

    def generator_init(self):
        self.camera = cv2.VideoCapture(0)

    def gen_frame(self):
        f,frame = self.camera.read()
        return [frame]

    def generator_finish(self):
        return

def key_reader():
    global key
    lock = threading.Lock()
    while True:
        with lock:
            key = getch()
        if key == 'q':
            break

def recive_and_sink_video(frameEditor, framesDst, framesSrc, frameMerger):
    threading.Thread(target = key_reader).start()
    while 1:
        framesSrc.generator_init()
        framesDst.sink_init()
        while 1:
            frames = framesSrc.gen_frame()
            frame = frameMerger.frame_merge(frames)
            frame = frameEditor.frame_edit(frame)
            if not framesDst.frame_sink(frame) or key == 'q':
                break
        framesDst.sink_finish()
        framesSrc.generator_finish()
        if key == 'q':
            break

