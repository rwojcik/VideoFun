from video_streaming_core import *

import sys

print "ts_shower"

fromhost = '127.0.0.1'
_from = 5006

try:
    print "sys.argv:"
    print sys.argv
    if '-fromhost' in sys.argv: fromhost = sys.argv[sys.argv.index('-fromhost') + 1]
    if '-from' in sys.argv:
        _from = sys.argv[sys.argv.index('-from') + 1]
        print "found -from"
    _from = int(_from)
    print "From %s:%s" % (fromhost, _from)
    recive_and_sink_video(frameEditor= FrameEditorEmpty(), framesDst= FrameSinkShower(), framesSrc= FrameGenearator(fromhost, _from))
except ValueError, e:
    print "You have to input -from and -to args"