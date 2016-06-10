start python block.py -framesource CameraFrameGenerator  -framedestination TransmissionControlSinkServer  localhost:5005  -editor FrameEditorEmpty 
start python block.py -framesource TransmissionControlFrameGenerator  localhost:5005  -editor FrameEditorEmpty 
