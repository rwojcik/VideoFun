from video_streaming_core import *

recive_and_sink_video(FrameEditorEllipse(), FrameSinkServer('127.0.0.1', 5006), FrameGenearator('127.0.0.1', 5005))