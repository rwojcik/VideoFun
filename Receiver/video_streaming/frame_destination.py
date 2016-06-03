from video_streaming_core import *
import sys


class DatagramSinkServer:

    def __init__(self, dst_host):
        self.socketInfos = list()
        for hostport in map(lambda x: (x.split(':')[0], int(x.split(':')[1])), dst_host.split(',')):
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            si = SocketInfo(hostport[0], hostport[1], s)
            self.socketInfos.append(si)

    def frame_sink(self, frame):
        retval, buf = cv2.imencode('.jpg', frame)
        if not retval:
            return False
        buf_str = '{}{}'.format('%08d' % len(buf), buf.tostring())  # TODO: encode int
        for si in self.socketInfos:
            try:
                print 'sending {} bytes'.format(buf_str[:8])
                self.split_and_sink(buf_str, si)
            except socket.error as e:
                print >> sys.stderr, '{}, buffer size: {}'.format(str(e), len(buf_str))
        return True

    def split_and_sink(self, buf_str, si):  # TODO: add order info
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


def try_send_tcp(si, buf_str):
    send = False
    while not send:
        try:
            si.s[1].send(buf_str)
            send = True
        except socket.error as e:
            print >> sys.stderr, '{}, retrying sending frame'.format(e)
            time.sleep(1)
            si.s[0].close()
            si.s[1].close()
            time.sleep(1)
            connected = False
            while not connected:
                try:
                    si.s[1].close()
                    si.s[0].close()
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind((si.ip, si.port))
                    s.listen(1)
                    conn, _ = s.accept()
                    si.s = (s, conn)
                    connected = True
                    print 'successfully reconnected'
                except socket.error as e:
                    print >> sys.stderr, '{}, retrying connection'.format(e)
                    time.sleep(1)


class TransmissionControlSinkServer:

    def __init__(self, dst_host):
        self.socketInfos = list()
        for hostport in map(lambda x: (x.split(':')[0], int(x.split(':')[1])), dst_host.split(',')):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((hostport[0], hostport[1]))
            s.listen(1)
            conn, _ = s.accept()
            si = SocketInfo(hostport[0], int(hostport[1]), (s, conn))
            self.socketInfos.append(si)

    def sink_finish(self):
        for si in self.socketInfos:
            si.s[0].close()  # s[0] - socket
            si.s[1].close()  # s[1] - connection

    def frame_sink(self, frame):
        try:
            retval, buf = cv2.imencode(".jpg", frame)
            if not retval:
                return False
            for si in self.socketInfos:
                buf_str = '{}{}{}'.format('%08d*' % len(buf), buf.tostring(), '*end')
                # si.s[1].send("%d*" % (buf.size))
                print 'sending {} bytes'.format(len(buf))
                try_send_tcp(si, buf_str)
        except (socket.error, cv2.error) as e:
            print >> sys.stderr, str(e)
        return True


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

