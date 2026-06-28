from smallblock.animation import AnimationClip, AnimationPlayer

clip = AnimationClip(
    ["Idle1", "Idle2", "Idle3", "Idle4"],
    fps=4,
    loop=True,
)

player = AnimationPlayer()
player.play(clip)

for i in range(12):
    player.update(0.25)
    print(i, player.current_frame)
