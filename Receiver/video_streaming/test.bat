start python block.py -editor FrameEditorGreyscale -framesource CameraFrameGenerator -framedestination DatagramSinkServer localhost:5005
start python block.py -framesource DatagramFrameGenerator localhost:5005 -editor FrameEditorFramesCounter