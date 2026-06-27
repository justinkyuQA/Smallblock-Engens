from smallblock.audio import sine, square, adsr, mix, write_wav

lead = adsr(sine(440, 1.0, 0.5))
bass = adsr(square(110, 1.0, 0.25))

song = mix([lead, bass])

write_wav("exports/smallblock_audio_v01.wav", song)

print("SmallBlock Audio Engine v0.1")
print("Generated: exports/smallblock_audio_v01.wav")
