def clamp(value,minimum,maximum):
    return max(minimum,min(maximum,value))

def lerp(a,b,t):
    return a+(b-a)*t
