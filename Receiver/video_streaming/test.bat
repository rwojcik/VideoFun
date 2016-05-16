start python ts_server.py -to 5005,5006
timeout 1
REM start python block.py -from 5005 -to 5006 -editor FrameEditorSmoothing
REM timeout 1
REM start python block.py -from 5006 -to 5007 -editor FrameEditorCircles
REM timeout 1
start python ts_shower.py -from 5005,5006 -merge FrameMergerStack
PAUSE
