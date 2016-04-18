start python video_streaming/ts_server.py -to 5005
timeout 1
start python video_streaming/block.py -from 5005 -to 5006 -editor FrameEditorEllipse
timeout 1
start python video_streaming/ts_shower.py -from 5006
PAUSE
