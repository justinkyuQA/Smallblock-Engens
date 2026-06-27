import math

SAMPLE_RATE = 44100

def sine(freq=440, seconds=1.0, volume=0.5):
    total = int(SAMPLE_RATE * seconds)
    return [
        volume * math.sin(2 * math.pi * freq * i / SAMPLE_RATE)
        for i in range(total)
    ]

def square(freq=440, seconds=1.0, volume=0.5):
    total = int(SAMPLE_RATE * seconds)
    return [
        volume if math.sin(2 * math.pi * freq * i / SAMPLE_RATE) >= 0 else -volume
        for i in range(total)
    ]
