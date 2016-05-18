import numpy as np, cv2


class FrameMergerFirst:
    def frame_merge(self, frames):
        if len(frames) == 0:
            img = np.zeros((512, 512, 3), np.uint8)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Empty image!', (10, 500), font, 1, (255, 255, 255), 2)
            return img
        return frames[0]


class FrameMergerStack:
    def frame_merge(self, frames):
        if len(frames) < 2:
            return FrameMergerFirst.frame_merge(frames[0])
        return np.concatenate((frames[0], frames[1]), axis=0)


class FrameMergerBlending:
    def frame_merge(self, frames):
        if len(frames) < 2:
            return FrameMergerFirst.frame_merge(frames[0])
        return cv2.addWeighted(frames[0], 0.5, frames[1], 0.5, 0)

