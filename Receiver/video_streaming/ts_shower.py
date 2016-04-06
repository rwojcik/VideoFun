from video_streaming_core import *

recive_and_sink_video(frameEditor= FrameEditorEmpty(), framesDst= FrameSinkShower(), framesSrc= FrameGenearator('127.0.0.1', 5006))