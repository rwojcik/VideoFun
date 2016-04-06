from video_streaming_core import *

print "Block started"
recive_and_sink_video(framesSrc= FrameGenearator('127.0.0.1', 5005), framesDst= FrameSinkServer('127.0.0.1', 5006), frameEditor= FrameEditorEllipse())