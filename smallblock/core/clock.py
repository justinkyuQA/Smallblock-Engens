import time

class Clock:

    def __init__(self):
        self.last=time.time()

    def tick(self):
        now=time.time()
        dt=now-self.last
        self.last=now
        return dt
