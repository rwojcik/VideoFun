import sys
from video_streaming_core import *

fromhost = '127.0.0.1'
tohost = '127.0.0.1'
editor = 'Empty'


def arg_val(arg_name):
    return sys.argv[sys.argv.index(arg_name) + 1]

def is_arg(argname):
    return argname in sys.argv

try:
    _from = arg_val('-from')
    _to = arg_val('-to')
    if is_arg('-fromhost'): fromhost = arg_val('-fromhost')
    if '-tohost' in sys.argv: tohost = arg_val('-tohost')
    if '-editor' in sys.argv: editor = arg_val('-editor')
    _from = int(_from)
    _to = int(_to)
    print "From %s:%s to %s:%s, edit by %s" % (fromhost, _from, tohost, _to, editor)
    #frameEditor= FrameEditorEllipse()
    frameEditor= eval(editor)()
    recive_and_sink_video(framesSrc= FrameGenearator(fromhost, _from), framesDst= FrameSinkServer(tohost, _to), frameEditor=frameEditor)
except ValueError, e:
    print "You have to input -from and -to args"