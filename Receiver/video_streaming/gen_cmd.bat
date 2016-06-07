start python block.py -framesource CameraFrameGenerator  -framedestination TransmissionControlSinkServer  localhost:5005  -editor FrameEditorEmpty 
start python block.py -framesource TransmissionControlFrameGenerator  localhost:5007  -editor FrameEditorEmpty 
start python block.py -framesource TransmissionControlFrameGenerator  localhost:5005 -framedestination TransmissionControlSinkServer  localhost:5006  -editor FrameEditorColorInversion
start python block.py -framesource TransmissionControlFrameGenerator  localhost:5006 -framedestination TransmissionControlSinkServer  localhost:5007  -editor FrameEditorFramesCounter
