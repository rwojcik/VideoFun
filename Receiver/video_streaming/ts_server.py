from video_streaming_core import *
from frame_editor import *
from frame_merge import *

import sys

print "ts_server"

tohost = '127.0.0.1'
_to = 5005

try:
    if '-tohost' in sys.argv: tohost = sys.argv[sys.argv.index('-tohost') + 1]
    if '-to' in sys.argv: _to = sys.argv[sys.argv.index('-to') + 1]
    print "To %s:%s" % (tohost, _to)
    recive_and_sink_video(frameEditor=FrameEditorEmpty(), framesDst=FrameSinkServer(tohost, _to), framesSrc=CameraFrameGenearator(), frameMerger=FrameMergerFirst())
except ValueError, e:
    print "You have to input -from and -to args"