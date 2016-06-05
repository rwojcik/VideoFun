# coding=utf-8
import calendar
import numpy as np, cv2
import time


class FrameEditorEmpty:
    # params nie są używane
    def __init__(self, params):
        pass

    def frame_edit(self, frame):
        return frame


class FrameEditorEllipse:
    # params[0] i params [1] - pozycja środka elipsy (0 <= x <= 1)
    def __init__(self, params):
        paramsSplit = params.split(',')
        if len(paramsSplit) > 1 and all(x.isdigit() for x in paramsSplit):
            self.params = map(lambda x: int(x), paramsSplit)
        else:
            self.params = [0.5, 0.5]
        pass

    def frame_edit(self, frame):
        height, width, _ = frame.shape
        cv2.ellipse(frame, (self.params[0] * width, self.params[1] * height), (100, 50), 0, 0, 180, 255, -1)
        return frame


class FrameEditorGreyscale:
    # params nie są używane
    def __init__(self, params):
        pass

    def frame_edit(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame


class FrameEditorResize:
    def __init__(self, params):
        paramsSplit = params.split(',')
        if len(paramsSplit) > 1 and all(x.isdigit() for x in paramsSplit):
            self.params = map(lambda x: int(x), paramsSplit)
        else:
            self.params = [0.7, 0.7]
        pass

    def frame_edit(self, frame):
        frame = cv2.resize(frame, (0, 0), fx=self.params[0], fy=self.params[1])
        return frame

class FrameEditorSmoothing:
    # params[0] i params [1] - zasięg rozmycia gaussowskiego
    def __init__(self, params):
        paramsSplit = params.split(',')
        if len(paramsSplit) >= 3 and all(x.isdigit() for x in paramsSplit):
            self.params = map(lambda x: int(x), paramsSplit)
            self.params[0] |= 1   # x | 1 zapewnia liczbę nieparzystą
            self.params[1] |= 1
        else:
            self.params = [11, 11, 0]
        pass

    def frame_edit(self, frame):
        print self.params
        if self.params[2] == 0:
            frame = cv2.GaussianBlur(frame, (self.params[0], self.params[1]), 0)
        elif self.params[2] == 1:
            frame = cv2.bilateralFilter(frame, 9, self.params[0], self.params[1])
        return frame


class FrameEditorDerivative:
    # params nie są używane
    def __init__(self, params):
        pass

    def frame_edit(self, frame):
        frame = cv2.Laplacian(frame, cv2.CV_64F)
        return frame


class FrameEditorCircles:
    # params[0] - dp
    # params[1] - minDist
    # params[2] - higher threshold
    # params[3] - accumulator threshold
    # params[4] - minRadius
    # params[5] - maxRadius
    def __init__(self, params):
        paramsSplit = params.split(',')
        if len(paramsSplit) >= 6 and all(x.isdigit() for x in paramsSplit):
            self.params = map(lambda x: int(x), paramsSplit)
        else:
            self.params = [2, 50, 100, 60, 50, 0]
        pass

    def frame_edit(self, frame):
        gsFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gsFrame, cv2.HOUGH_GRADIENT, dp=self.params[0], minDist=self.params[1],
                                   param1=self.params[2], param2=self.params[3], minRadius=self.params[4],
                                   maxRadius=self.params[5])
        if circles is None:
            return frame
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv2.circle(img=frame, center=(i[0], i[1]), radius=i[2], color=(128, 128, 128, 128), thickness=1)
            cv2.circle(img=frame, center=(i[0], i[1]), radius=2, color=(64, 64, 64, 128), thickness=1)
        return frame


class FrameEditorFramesCounter:
    # params nie są używane
    def __init__(self, params):
        self.lastFlush = calendar.timegm(time.gmtime())
        self.frames = 0
        self.framesTxt = ''
        self.font = cv2.FONT_HERSHEY_DUPLEX

    def frame_edit(self, frame):
        self.frames += 1
        timeDiff = calendar.timegm(time.gmtime()) - self.lastFlush
        if timeDiff >= 1:
            self.framesTxt = str(self.frames / timeDiff)
            self.lastFlush = calendar.timegm(time.gmtime())
            self.frames = 0
        cv2.putText(img=frame, text=self.framesTxt, org=(10, 30), fontFace=self.font, fontScale=1, color=(0, 0, 255),
                    thickness=1)
        return frame


class FrameEditorMedianStack:
    def __init__(self, params):
        paramsSplit = params.split(',')
        if len(paramsSplit) >= 1 and all(x.isdigit() for x in paramsSplit):
            self.memory_size = int(paramsSplit[0])
        else:
            self.memory_size = 5
        self.frames_memory = []
        self.last_pos = 0

    def frame_edit(self, frame):
        if len(self.frames_memory) < self.memory_size:
            self.frames_memory.append(frame)
            height, width, depth = frame.shape
            img = np.zeros((height, width, depth), np.uint8)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img=img, text='Initializing median stack...', org=(10, height-10), fontFace=font, fontScale=1, color=(255, 255, 255), thickness=2)
            return img
        background = np.median(self.frames_memory, axis=0).astype(np.int8)
        self.frames_memory[self.last_pos] = frame
        self.last_pos = (self.last_pos + 1) % self.memory_size
        return background


def diff_img(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)


def num_to_bgr(value):
    r = (value >> 16) & 0xFF
    g = (value >> 8) & 0xFF
    b = value & 0xFF
    return b, g, r


class FrameEditorMovementDetection:
    def __init__(self, params):
        # params[0] - kolor (0xRRGGBB) zaznaczenia
        self.frames_memory = []
        self.last_pos = 0
        if len(params.split(',')) >= 1 and all(x.isdigit() for x in params.split(',')):
            params = map(lambda x: int(x), params.split(','))
            self.color = num_to_bgr(params[0])
        else:
            self.color = num_to_bgr(16777215)
        pass

    def frame_edit(self, frame):
        height, width, depth = frame.shape
        if len(self.frames_memory) < 3:
            self.frames_memory.append(frame)
            img = np.zeros((height, width, depth), np.uint8)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img=img, text='Initializing background image...', org=(10, height - 10), fontFace=font, fontScale=1, color=(255, 255, 255), thickness=2)
            return img
        t_minus = cv2.cvtColor(self.frames_memory[(self.last_pos+3) % 3], cv2.COLOR_RGB2GRAY)
        t = cv2.cvtColor(self.frames_memory[(self.last_pos+4) % 3], cv2.COLOR_RGB2GRAY)
        t_plus = cv2.cvtColor(self.frames_memory[(self.last_pos+5) % 3], cv2.COLOR_RGB2GRAY)
        self.frames_memory[self.last_pos] = frame.copy()
        self.last_pos = (self.last_pos + 1) % 3
        movement_mask = diff_img(t_minus, t, t_plus)
        thresh = cv2.threshold(movement_mask, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        _, contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(image=frame, contours=contours, contourIdx=-1, color=self.color, thickness=-1)
        return frame




