#!/usr/bin/env python

import socket
from editor import *
from merge import *
import sys

DATAGRAM_MAX_SIZE = 65507

key = ''


class SocketInfo:

    def __init__(self, ip, port, s):
        self.ip = ip
        self.port = port
        self.s = s  # for TCP - tuple (socket, connection), UDP - socket only


def receive_and_sink_video(frameEditor, framesDst, framesSrc, frameMerger):
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

