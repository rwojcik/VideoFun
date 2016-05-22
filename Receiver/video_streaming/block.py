import sys
from video_streaming_core import *
from frame_merge import *
from frame_editor import *

print "block"

fromhost = '127.0.0.1'
tohost = '127.0.0.1'
editor = 'Empty'
merge = 'FrameMergerFirst'
editorparams = ''
mergerparams = ''

try:
    _from = sys.argv[sys.argv.index('-from') + 1]
    _to = sys.argv[sys.argv.index('-to') + 1]
    if '-fromhost' in sys.argv: fromhost = sys.argv[sys.argv.index('-fromhost') + 1]
    if '-tohost' in sys.argv: tohost = sys.argv[sys.argv.index('-tohost') + 1]
    if '-editor' in sys.argv: editor = sys.argv[sys.argv.index('-editor') + 1]
    if '-merge' in sys.argv: merge = sys.argv[sys.argv.index('-merge') + 1]
    if '-editorparams' in sys.argv: editorparams = sys.argv[sys.argv.index('-editorparams') + 1]
    if '-mergerparams' in sys.argv: mergerparams = sys.argv[sys.argv.index('-mergerparams') + 1]
    print "From %s:%s to %s:%s, edit by %s" % (fromhost, _from, tohost, _to, editor)
    frameEditor = eval(editor)(editorparams)
    frameMerger = eval(merge)(mergerparams)
    recive_and_sink_video(framesSrc=FrameGenerator(fromhost, _from), framesDst=FrameSinkServer(tohost, _to), frameEditor=frameEditor, frameMerger=frameMerger)
except ValueError, e:
    print e