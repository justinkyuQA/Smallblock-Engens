import wave
import struct

SAMPLE_RATE = 44100

def write_wav(path, samples):
    with wave.open(path, "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)

        for sample in samples:
            sample = max(-1.0, min(1.0, sample))
            wav.writeframes(struct.pack("<h", int(sample * 32767)))
