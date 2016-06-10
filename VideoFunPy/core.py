#!/usr/bin/env python

import socket
from editor import *
from merge import *
import sys

DATAGRAM_MAX_SIZE = 65507

key = ''


class SocketInfo:
    """
    Simple type which holds information about connection and socket.

    :param ip: specifies ip or host.
    :param port: specifies port.
    :param s: holds socket if used in user datagram protocol or socket and connection used in transmission control
    protocol.
    """
    def __init__(self, ip, port, s):
        self.ip = ip
        self.port = port
        self.s = s  # for TCP - tuple (socket, connection), UDP - socket only


def receive_and_sink_video(frameEditor, framesDst, framesSrc, frameMerger):
    """
    Loops through frames source, merger, editor and sink.
    Continuously provides service.

    :param frameEditor: instance of editor.
    :param framesDst: instance of frame sink.
    :param framesSrc: instance of frames source
    :param frameMerger: instance of frames merger.
    """
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

