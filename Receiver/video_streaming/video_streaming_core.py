#!/usr/bin/env python

import socket
from UserString import MutableString
import cv2
import numpy as np
import threading, time
from frame_editor import *
from frame_merge import *
from msvcrt import getch
from itertools import *
import sys

DATAGRAM_MAX_SIZE = 65507

key = ''


class FrameSinkShower:
    def frame_sink(self, frame):
        global key
        try:
            cv2.imshow('frame', frame)
        except cv2.error as e:
            print >> sys.stderr, '{}, improper decoding'.format(str(e))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            key = 'q'
            return False
        return True

    def sink_finish(self):
        cv2.destroyWindow('frame')

    def __del__(self):
        self.sink_finish()


class SocketInfo:

    def __init__(self, ip, port, s):
        self.ip = ip
        self.port = port
        self.s = s


class FrameSinkServer:

    def __init__(self, ip, ports):
        self.ip = ip
        self.socketInfos = list()
        for port in map(lambda x: int(x), ports.split(",")):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            si = SocketInfo(self.ip, port, s)
            self.socketInfos.append(si)

    def sink_finish(self):
        for si in self.socketInfos:
            si.s.close()

    def frame_sink(self, frame):
        retval, buf = cv2.imencode('.jpg', frame)
        if not retval:
            return False
        buf_str = buf.tostring()
        for si in self.socketInfos:
            try:
                # send info about length
                si.s.sendto('{}'.format(len(buf_str)), (si.ip, si.port))
                print 'sent {}* string length'.format(len(buf_str))
                self.split_and_sink(buf_str, si)
            except socket.error as e:
                print >> sys.stderr, '{}, buffer size: {}'.format(str(e), len(buf_str))
        return True

    def split_and_sink(self, buf_str, si):
        if len(buf_str) > DATAGRAM_MAX_SIZE:
            # recursive string splitting and sending, first udp message carries length
            self.split_and_sink(buf_str[:DATAGRAM_MAX_SIZE], si)
            self.split_and_sink(buf_str[DATAGRAM_MAX_SIZE:], si)
        else:
            si.s.sendto(buf_str, (si.ip, si.port))
            print '\tsent {} bytes'.format(len(buf_str))

    def sink_finish(self):
        for si in self.socketInfos:
            si.s.close()

    def __del__(self):
        self.sink_finish()


def recv_data(si):
    img = []
    read = False
    while not read:
        try:
            frame_str = ''
            data_len = read_number(si)
            number = data_len
            print 'trying to read data, size: {}'.format(number)
            while number > 0:
                # read as much as UDP allows
                to_read = min(DATAGRAM_MAX_SIZE, number)
                print '\treading part, size: {}'.format(to_read)
                frame_part, _ = si.s.recvfrom(to_read)
                if len(frame_part) != to_read:
                    # ignore message if length is incorrect, it's already lost
                    print >> sys.stderr, '\tlost frame...'
                    break
                frame_str += frame_part
                number -= len(frame_part)
            if len(frame_str) == data_len:
                nparr = np.fromstring(frame_str, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                read = True
        except socket.error as e:
            print >> sys.stderr, '{}error reading frames, retry'.format(str(e))
    return img


def read_number(si):
    # ch = ''.join(takewhile(lambda x: x.isdigit(), ch))
    read = False
    while not read:
        try:
            ch, _ = si.s.recvfrom(1024)
            number = int(ch)
            read = True
        except:
            # retry on failed read or failed cast
            pass
    return number


class FrameGenerator:

    def __init__(self, ip, port):
        self.ip = ip
        self.socketInfos = list()
        for port in map(lambda x: int(x), port.split(",")):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind((self.ip, port))
            si = SocketInfo(self.ip, port, s)
            self.socketInfos.append(si)

    def gen_frame(self):
        frames = list()
        try:
            for si in self.socketInfos:
                frame_data = recv_data(si)
                frames.append(frame_data)
        except socket.error as e:
            print >> sys.stderr, "{}, frame(s) was lost".format(str(e))
        return frames

    def generator_finish(self):
        for si in self.socketInfos:
            si.s.close()

    def __del__(self):
        self.generator_finish()

class CameraFrameGenerator:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def gen_frame(self):
        _, frame = self.camera.read()
        return [frame]

    def generator_finish(self):
        pass

    def __del__(self):
        self.generator_finish()


def recive_and_sink_video(frameEditor, framesDst, framesSrc, frameMerger):
    global key
    while 1:
        frames = framesSrc.gen_frame()
        frame = frameMerger.frame_merge(frames)
        frame = frameEditor.frame_edit(frame)
        if not framesDst.frame_sink(frame) or key == 'q':
            break
    print 'closing program'
    framesDst.sink_finish()
    framesSrc.generator_finish()

