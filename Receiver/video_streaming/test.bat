start python ts_server.py -to 5005,5006
start python block.py -from 5005 -to 5008 -editor FrameEditorSmoothing
start python block.py -from 5006 -to 5009 -editor FrameEditorCircles
start python block.py -from 5008,5009 -to 5010 -merge FrameMergerBlending -editor FrameEditorFramesCounter
start python ts_shower.py -from 5010
