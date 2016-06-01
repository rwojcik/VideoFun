start python ts_server.py -to 5005
start python block.py -from 5005 -to 5007 -editor FrameEditorGreyscale
start python block.py -from 5007 -to 5008 -editor FrameEditorFramesCounter
start python ts_shower.py -from 5008