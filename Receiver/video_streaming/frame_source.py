
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


class SocketFrameGenerator:

    def __init__(self, src_host):
        self.socketInfos = list()
        for hostport in map(lambda x: (x.split(':')[0], x.split(':')[1]), src_host.split(',')):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip = hostport[0]
            port = int(hostport[1])
            s.bind((ip, port))
            si = SocketInfo(ip, port, s)
            self.socketInfos.append(si)

    def generator_init(self):
        for port in self.ports:
            self._connect_and_append_port(port)

    def _connect_and_append_port(self, port):
        while True:
             try:
                  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                  s.connect((self.ip, int(port)))
                  self.sockets.append(s)
                  return
             except socket.error:
                 print "socket.error, sleep and retry"
                 time.sleep(0.5)

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
