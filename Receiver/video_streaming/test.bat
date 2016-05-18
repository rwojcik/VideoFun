start python ts_server.py -to 5005,5006
timeout 1
start python block.py -from 5005 -to 5008 -editor FrameEditorSmoothing
timeout 1
start python block.py -from 5006 -to 5009 -editor FrameEditorCircles
timeout 1
start python ts_shower.py -from 5008,5009 -merge FrameMergerBlending
PAUSE
