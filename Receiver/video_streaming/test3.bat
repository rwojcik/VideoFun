start python block.py  -framesource CameraFrameGenerator -framedestination DatagramSinkServer localhost:5005,localhost:5006
start python block.py -framesource DatagramFrameGenerator localhost:5005 -framedestination DatagramSinkServer localhost:5007 -editor FrameEditorGreyscale
start python block.py -framesource DatagramFrameGenerator localhost:5006 -framedestination DatagramSinkServer localhost:5008 -editor FrameEditorSmoothing -editorparams 30,30,0
start python block.py -framesource DatagramFrameGenerator localhost:5007,localhost:5008 -editor FrameEditorFramesCounter -merge FrameMergerStack