from video_streaming_core import *
from frame_editor import *
from frame_merge import *

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
    if '-merge' in sys.argv: merge = sys.argv[sys.argv.index('-merge') + 1]
    _from = int(_from)
    print "From %s:%s" % (fromhost, _from)
    frameMerger=eval(merge) ()
    recive_and_sink_video(frameEditor= FrameEditorEmpty(), framesDst= FrameSinkShower(), framesSrc= FrameGenerator(fromhost, _from), frameMerger=frameMerger)
except ValueError, e:
    print "You have to input -from and -to args"