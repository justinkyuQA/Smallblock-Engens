class AnimationPlayer:

    def __init__(self):
        self.clip = None
        self.frame = 0
        self.timer = 0.0
        self.playing = False

    def play(self, clip):
        self.clip = clip
        self.frame = 0
        self.timer = 0.0
        self.playing = True

    def stop(self):
        self.playing = False
        self.frame = 0
        self.timer = 0.0

    def pause(self):
        self.playing = False

    def resume(self):
        if self.clip:
            self.playing = True

    def update(self, dt):
        if not self.playing or self.clip is None:
            return

        self.timer += dt

        while self.timer >= self.clip.frame_time:
            self.timer -= self.clip.frame_time
            self.frame += 1

            if self.frame >= len(self.clip.frames):
                if self.clip.loop:
                    self.frame = 0
                else:
                    self.frame = len(self.clip.frames) - 1
                    self.playing = False

    @property
    def current_frame(self):
        if self.clip is None:
            return None
        return self.clip.frames[self.frame]
