start python ts_server.py -to 5005,5006
start python ts_shower.py -from 5007,5008 -merge FrameMergerStack
start python ts_shower.py
start python block.py -from 5005 -to 5007  -editor FrameEditorSmoothing  -editorparams 11,11,1
start python block.py -from 5006 -to 5008  -editor FrameEditorGreyscale
