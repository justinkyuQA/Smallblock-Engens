class AnimationClip:

    def __init__(self, frames, fps=8, loop=True):
        self.frames = list(frames)
        self.fps = fps
        self.loop = loop

    @property
    def frame_time(self):
        return 1.0 / self.fps
