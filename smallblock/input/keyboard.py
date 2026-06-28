import os
import sys

if os.name != "nt":
    import tty
    import termios
    import select


class Keyboard:

    def poll(self):

        if os.name == "nt":
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getwch()
            return None

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)

        try:
            tty.setcbreak(fd)

            ready, _, _ = select.select([sys.stdin], [], [], 0)

            if ready:
                return sys.stdin.read(1)

            return None

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
