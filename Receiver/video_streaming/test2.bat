start python block.py -editor FrameEditorGreyscale -framesource CameraFrameGenerator -framedestination TransmissionControlSinkServer localhost:5005,localhost:5006
start python block.py -framesource TransmissionControlFrameGenerator localhost:5005 -framedestination TransmissionControlSinkServer localhost:5007 -editor FrameEditorCircles
start python block.py -framesource TransmissionControlFrameGenerator localhost:5006 -framedestination TransmissionControlSinkServer localhost:5008 -editor FrameEditorSmoothing
start python block.py -framesource TransmissionControlFrameGenerator localhost:5007,localhost:5008 -editor FrameEditorFramesCounter -merge FrameMergerBlending
