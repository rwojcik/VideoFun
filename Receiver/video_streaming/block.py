import sys
from video_streaming_core import *

print "block"

fromhost = '127.0.0.1'
tohost = '127.0.0.1'
editor = 'Empty'


try:
    _from = sys.argv[sys.argv.index('-from') + 1]
    _to = sys.argv[sys.argv.index('-to') + 1]
    if '-fromhost' in sys.argv: fromhost = sys.argv[sys.argv.index('-fromhost') + 1]
    if '-tohost' in sys.argv: tohost = sys.argv[sys.argv.index('-tohost') + 1]
    if '-editor' in sys.argv: editor = sys.argv[sys.argv.index('-editor') + 1]
    _from = int(_from)
    _to = int(_to)
    print "From %s:%s to %s:%s, edit by %s" % (fromhost, _from, tohost, _to, editor)
    #frameEditor= FrameEditorEllipse()
    frameEditor= eval(editor)()
    recive_and_sink_video(framesSrc= FrameGenearator(fromhost, _from), framesDst= FrameSinkServer(tohost, _to), frameEditor=frameEditor)
except ValueError, e:
    print "You have to input -from and -to args"