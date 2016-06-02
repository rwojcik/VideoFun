# coding=utf-8
import numpy as np, cv2


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
        self.frames = []

    def frame_merge(self, frames):
        if len(frames) < 2:
            if len(self.frames) >= 2:
                # pokaż historię, jeżeli jest za mało ramek
                return np.concatenate((self.frames[0], self.frames[1]), axis=0)
            else:
                return FrameMergerFirst.frame_merge(frames[0])
        return np.concatenate((frames[0], frames[1]), axis=0)


class FrameMergerBlending:
    #params[0] - waga złączenia (0 <= x <= 1)
    def __init__(self, params):
        paramsSplit = params.split(',')
        if len(paramsSplit) >= 1 and all(x.isdigit() for x in paramsSplit) and 0 <= paramsSplit[0] <= 1:
            self.params = int(paramsSplit)
        else:
            self.params = [0.5]
        pass

    def frame_merge(self, frames):
        if len(frames) < 2:
            return FrameMergerFirst.frame_merge(frames[0])
        return cv2.addWeighted(frames[0], self.params[0], frames[1], 1 - self.params[0], 0)

