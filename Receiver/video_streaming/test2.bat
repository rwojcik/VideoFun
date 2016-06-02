start python block.py -editor FrameEditorGreyscale -framesource CameraFrameGenerator -framedestination FrameSinkServer localhost:5005,localhost:5006
start python block.py -framesource SocketFrameGenerator localhost:5005 -framedestination FrameSinkServer localhost:5007 -editor FrameEditorCircles
start python block.py -framesource SocketFrameGenerator localhost:5006 -framedestination FrameSinkServer localhost:5008 -editor FrameEditorSmoothing
start python block.py -framesource SocketFrameGenerator localhost:5007,localhost:5008 -editor FrameEditorFramesCounter -merge FrameMergerBlending
