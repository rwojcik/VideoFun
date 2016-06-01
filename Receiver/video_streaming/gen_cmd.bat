start python ts_server.py -to 5005
start python ts_shower.py -from 5008,5009 -merge FrameMergerStack
start python block.py -from 5005 -to 5006,5007  -editor FrameEditorResize  -editorparams 0.3000,0.5000
start python block.py -from 5006 -to 5008  -editor FrameEditorSmoothing  -editorparams 11,11,0
start python block.py -from 5007 -to 5009  -editor FrameEditorGreyscale
