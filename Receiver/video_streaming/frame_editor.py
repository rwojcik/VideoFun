import numpy as np, cv2

class FrameEditorEmpty:
    def frame_edit(self, frame):
        return frame

class FrameEditorEllipse:
    def frame_edit(self, frame):
        cv2.ellipse(frame,(256,256),(100,50),0,0,180,255,-1)
        return frame

class FrameEditorGreyscale:
    def frame_edit(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame

class FrameEditorSmoothing:
    def frame_edit(self, frame):
        frame = cv2.GaussianBlur(frame, (11, 11), 0)
        return frame

class FrameEditorDerivative:
    def frame_edit(self, frame):
        frame = cv2.Laplacian(frame, cv2.CV_64F)
        return frame

class FrameEditorCircles:
    def frame_edit(self, frame):
        gsFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gsFrame, cv2.HOUGH_GRADIENT, dp=2, minDist=50, param1=100, param2=60, minRadius=50, maxRadius=0)
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(img=frame,center=(i[0],i[1]),radius=i[2],color=(128,128,128,128),thickness=1)
            cv2.circle(img=frame,center=(i[0],i[1]),radius=2,color=(64,64,64,128),thickness=1)
        return frame