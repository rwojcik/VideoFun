start python ts_server.py -to 5005
timeout /t 1
timeout /t 1start python block.py -from 5005 -to 5006 -editor FrameEditorSmoothing
timeout /t 1
start python block.py -from 5006 -to 5007 -editor FrameEditorCircles
timeout /t 1
start python ts_shower.py -from 5007


exit
