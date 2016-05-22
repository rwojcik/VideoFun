start python ts_server.py -to 5005
timeout 1
start python block.py -from 5005 -to 5006 -editor FrameEditorFramesCounter
timeout 1
start python ts_shower.py -from 5006