from video_streaming_core import *
from frame_editor import *
from frame_merge import *

import sys

print "ts_shower"

fromhost = '127.0.0.1'
mergerparams = ''
_from = 5006
merge = 'FrameMergerFirst'

try:
    print "sys.argv:"
    print sys.argv
    if '-fromhost' in sys.argv: fromhost = sys.argv[sys.argv.index('-fromhost') + 1]
    if '-from' in sys.argv: _from = sys.argv[sys.argv.index('-from') + 1]
    if '-merge' in sys.argv: merge = sys.argv[sys.argv.index('-merge') + 1]
    if '-mergerparams' in sys.argv: mergerparams = sys.argv[sys.argv.index('-mergerparams') + 1]
    print "From %s:%s" % (fromhost, _from)
    frameMerger = eval(merge) (mergerparams)
    recive_and_sink_video(frameEditor = FrameEditorEmpty(''), framesDst= FrameSinkShower(), framesSrc= FrameGenerator(fromhost, _from), frameMerger=frameMerger)
except ValueError, e:
    print e