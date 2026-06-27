def mix(tracks):
    if not tracks:
        return []

    max_len = max(len(t) for t in tracks)
    output = [0.0] * max_len

    for track in tracks:
        for i, sample in enumerate(track):
            output[i] += sample

    peak = max(abs(s) for s in output) or 1.0
    if peak > 1.0:
        output = [s / peak for s in output]

    return output
