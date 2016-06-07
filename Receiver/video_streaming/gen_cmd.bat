start python ts_server.py -to 5013
start python ts_shower.py -from 5015,5016 -merge FrameMergerStack
start python block.py -from 5013 -to 5014,5016  -editor FrameEditorResize  -editorparams 0.7000,0.7000
start python block.py -from 5014 -to 5015  -editor FrameEditorSmoothing  -editorparams 11,11,0
