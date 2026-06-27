SAMPLE_RATE = 44100

def adsr(samples, attack=0.05, decay=0.1, sustain=0.7, release=0.15):
    total = len(samples)
    a = int(SAMPLE_RATE * attack)
    d = int(SAMPLE_RATE * decay)
    r = int(SAMPLE_RATE * release)
    s_start = a + d
    r_start = max(0, total - r)

    out = []

    for i, sample in enumerate(samples):
        if a > 0 and i < a:
            amp = i / a
        elif d > 0 and i < s_start:
            t = (i - a) / d
            amp = 1.0 - t * (1.0 - sustain)
        elif r > 0 and i >= r_start:
            t = (i - r_start) / r
            amp = sustain * (1.0 - t)
        else:
            amp = sustain

        out.append(sample * amp)

    return out
