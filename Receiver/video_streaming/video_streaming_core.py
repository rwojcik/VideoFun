#!/usr/bin/env python

import socket
from frame_editor import *
from frame_merge import *
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
        buf_str = '{}{}'.format('%08d' % len(buf), buf.tostring())
        for si in self.socketInfos:
            try:
                print 'sending {} bytes'.format(buf_str[:8])
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
    frame_str = ''
    read = False
    while not read:
        try:
            frame_str = ''
            last = False
            while not last:
                if len(frame_str) > 0 and not frame_str[:5].isdigit():
                    # if frame_str doesn't start with digits then we have lost frame
                    print >> sys.stderr, 'frame_str doesn\'t begin with digits, frame(s) lost'
                    frame_str = ''
                # read as much as UDP allows
                frame_part, _ = si.s.recvfrom(DATAGRAM_MAX_SIZE)
                frame_str += frame_part
                last = len(frame_part) != DATAGRAM_MAX_SIZE
            if not frame_str[:8].isdigit():
                print >> sys.stderr, 'incorrect data, frame lost'
                continue
            data_len = int(frame_str[:8])
            frame = frame_str[8:]
            if len(frame) == data_len:
                nparr = np.fromstring(frame, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                read = True
            else:
                print >> sys.stderr, 'length data do not match, expected: {}, got: {}, diff: {}'.format(data_len, len(frame), len(frame) - data_len)
        except Exception as e:
            print >> sys.stderr, '{}error reading frames, retry'.format(str(e))
    print 'read image, size: {}'.format(len(frame_str))
    return img


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

