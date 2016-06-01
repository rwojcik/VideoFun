start python ts_server.py -to 5005,5006
start python ts_shower.py -from 5005,5007 -merge FrameMergerBlending -mergerparams 0.8 
start python block.py -from 5006 -to 5007  -editor FrameEditorDerivative
