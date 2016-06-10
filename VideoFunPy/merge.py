# coding=utf-8
import numpy as np, cv2
from editor import FrameEditorResize


class FrameMergerFirst:
    # params nie są używane
    def __init__(self, params):
        pass

    def frame_merge(self, frames):
        if len(frames) == 0:
            img = np.zeros((512, 512, 3), np.uint8)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Empty image!', (10, 500), font, 1, (255, 255, 255), 2)
            return img
        return frames[0]


class FrameMergerStack:
    # params nie są używane
    def __init__(self, params):
        self.history = None
        self.resizer = FrameEditorResize('')
        self.merger_first = FrameMergerFirst(0)

    def frame_merge(self, frames):
        if len(frames) < 2:
            if self.history is not None:
                # show history in case there is history shortage
                return self.history
            else:
                return self.merger_first.frame_merge(frames)
        if np.shape(frames[0])[1] != np.shape(frames[1])[1]:
            if np.shape(frames[0])[1] > np.shape(frames[1])[1]:
                factor = np.shape(frames[1])[1] / float(np.shape(frames[0])[1])
                self.resizer.params = [factor, factor]
                frames[0] = self.resizer.frame_edit(frames[0])
            else:
                factor = np.shape(frames[0])[1] / float(np.shape(frames[1])[1])
                self.resizer.params = [factor, factor]
                frames[1] = self.resizer.frame_edit(frames[1])
        self.history = np.concatenate((frames[0], frames[1]), axis=0)
        return self.history


class FrameMergerBlending:
    # params[0] - waga złączenia (0 <= x <= 1)
    def __init__(self, params):
        paramsSplit = params.split(',')
        if len(paramsSplit) >= 1 and all(x.isdigit() for x in paramsSplit) and 0 <= paramsSplit[0] <= 1:
            self.params = int(paramsSplit)
        else:
            self.params = [0.5]
        self.history = None
        self.resizer = FrameEditorResize('')
        self.merger_first = FrameMergerFirst(0)

    def frame_merge(self, frames):
        if len(frames) < 2:
            if self.history is not None:
                # show history in case there is history shortage
                return self.history
            else:
                return self.mereger_first.frame_merge(frames)
        if np.shape(frames[0])[1] != np.shape(frames[1])[1]:
            if np.shape(frames[0])[1] > np.shape(frames[1])[1]:
                factor = np.shape(frames[1])[1] / float(np.shape(frames[0])[1])
                self.resizer.params = [factor, factor]
                frames[0] = self.resizer.frame_edit(frames[0])
            else:
                factor = np.shape(frames[0])[1] / float(np.shape(frames[1])[1])
                self.resizer.params = [factor, factor]
                frames[1] = self.resizer.frame_edit(frames[1])
        self.history = cv2.addWeighted(frames[0], self.params[0], frames[1], 1 - self.params[0], 0)
        return self.history

