from video_streaming_core import *

recive_and_sink_video(FrameEditorEmpty(), FrameSinkShower(), FrameGenearator('127.0.0.1', 5006))