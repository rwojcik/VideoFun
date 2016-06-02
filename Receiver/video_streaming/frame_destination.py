
from video_streaming_core import *
import sys


class FrameSinkServer:

    def __init__(self, dst_host):
        self.socketInfos = list()
        for hostport in map(lambda x: (x.split(':')[0], x.split(':')[1]), dst_host.split(',')):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            si = SocketInfo(hostport[0], int(hostport[1]), s)
            self.socketInfos.append(si)

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

class FrameSinkShower:

    def __init__(self, dst_host):
        pass

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

