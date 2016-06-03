from UserString import MutableString
from itertools import takewhile
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

import struct

from video_streaming_core import *
import sys


class CameraFrameGenerator:
    def __init__(self, src_host):
        self.camera = cv2.VideoCapture(0)

    def gen_frame(self):
        _, frame = self.camera.read()
        return [frame]

    def generator_finish(self):
        pass

    def __del__(self):
        self.generator_finish()


def check_sequence(messages_no):
    max_v = max(messages_no)
    return set(messages_no) == set(range(0, max_v+1))


class DatagramFrameGenerator:

    def __init__(self, src_host):
        self.socket_infos = list()
        for host_port in map(lambda x: (x.split(':')[0], int(x.split(':')[1])), src_host.split(',')):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip = host_port[0]
            port = host_port[1]
            s.bind((ip, port))
            si = SocketInfo(ip, port, s)
            self.socket_infos.append(si)

    def gen_frame(self):
        frames = list()
        try:
            for si in self.socket_infos:
                frame_data = self.recv_udp_data(si)
                frames.append(frame_data)
        except socket.error as e:
            print >> sys.stderr, "{}, frame(s) was lost".format(str(e))
        return frames

    def generator_finish(self):
        for si in self.socket_infos:
            si.s.close()

    def __del__(self):
        self.generator_finish()

    def recv_udp_data(self, si):
        img = []
        frame_str = ''
        read = False
        message_buffer = Q.PriorityQueue()
        messages_no = []
        frame_no = 0
        while not read:  # TODO: buffer frames and reorder them by number
            try:
                frame_str = ''
                last = False
                got_end = False
                while not last:
                    # if len(frame_str) > 0 and not frame_str[8] == '*':
                    #     # if frame_str doesn't start with digits then we have lost frame
                    #     print >> sys.stderr, 'frame_str doesn\'t begin with packet length, frame(s) lost'
                    #     frame_str = ''
                    # read as much as UDP allows
                    frame_part, _ = si.s.recvfrom(DATAGRAM_MAX_SIZE)
                    frame_no_temp, message_no = struct.unpack("!2Q", frame_part[:16])
                    if frame_no_temp > frame_no:
                        message_buffer = Q.PriorityQueue()
                        messages_no = []
                        got_end = False
                    got_end |= len(frame_part) >= 4 and frame_part[len(frame_part)-4:] == '*end'
                    message_buffer.put((message_no, frame_part[17:]))
                    messages_no.append(message_no)
                    last = got_end and check_sequence(messages_no)
                # if not frame_str[8] == '*':
                #     print >> sys.stderr, 'frame_str doesn\'t begin with packet length, frame(s) lost'
                #     continue
                # data_len = struct.unpack('!Q', frame_str[:8])[0]  # decode as ull in network (b.endian) byte order
                # frame = frame_str[9:]
                # if len(frame) == data_len:
                while not message_buffer.empty():
                    frame_str += message_buffer.get()[1]
                nparr = np.fromstring(frame_str[:len(frame_str)-4], np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                read = True
                # else:
                #     print >> sys.stderr, 'length data do not match, expected: {}, got: {}, diff: {}' \
                #         .format(data_len, len(frame), len(frame) - data_len)
            except Exception as e:
                print >> sys.stderr, '{}error reading frames, retry'.format(str(e))
        print 'read image, size: {}'.format(len(frame_str))
        return img

def recv_tcp_data(si):
    frame_str = ''
    last = False
    while not last:
        received = False
        while not received:
            try:
                frame_part, _ = si.s.recvfrom(1024*100)
                received = True
            except socket.error as e:
                print >> sys.stderr, '{}, retrying receive frame'.format(e)
                frame_str = ''
                time.sleep(1)
                si.s.close()
                connected = False
                while not connected:
                    try:
                        si.s.close()
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((si.ip, si.port))
                        si.s = s
                        connected = True
                        print 'successfully reconnected'
                    except socket.error as e:
                        print >> sys.stderr, '{}, retrying connection'.format(e)
                        time.sleep(1)
        frame_str += frame_part
        last = frame_part[len(frame_part)-4:] == '*end'
    data_length = int(frame_str[:8])
    frame = frame_str[9:len(frame_str)-4]
    nparr = np.fromstring(frame, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def connect_tcp(ip, port):
    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            return SocketInfo(ip, port, s)
        except socket.error as e:
            print >> sys.stderr, '{}, sleep and retry'.format(str(e))
            time.sleep(0.5)


class TransmissionControlFrameGenerator:

    def __init__(self, src_host):
        self.socketInfos = list()
        for hostport in map(lambda x: (x.split(':')[0], int(x.split(':')[1])), src_host.split(',')):
            ip = hostport[0]
            port = hostport[1]
            si = connect_tcp(ip, port)
            # si = SocketInfo(ip, port, s)
            self.socketInfos.append(si)

    def gen_frame(self):
        frames = list()
        for si in self.socketInfos:
            # si.s.send('o')
            frame_data = recv_tcp_data(si)
            frames.append(frame_data)
        return frames

    def generator_finish(self):
        for s in self.socketInfos:
            s.s.close()