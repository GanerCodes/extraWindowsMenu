import colorsys, math

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def color(red, green, blue):
    red   = constrain(int(red)  , 0, 255) * 256 ** 2
    green = constrain(int(green), 0, 255) * 256
    blue  = constrain(int(blue) , 0, 255)
    return "#" + hex(red + green + blue)[2:].zfill(6)
    
def hsb(h, s, b):
    t = colorsys.hsv_to_rgb(h / 255, s / 255, b / 255)
    return color(t[0] * 255, t[1] * 255, t[2] * 255)

def dist(x1, y1, x2, y2):
	return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def mp(x1, y1, x2, y2):
	return [(x1 + x2) / 2, (y1 + y2) / 2]

def expand(c, s):
	return [c[0] - s, c[1] - s, c[2] + s, c[3] + s]