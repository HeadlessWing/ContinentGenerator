def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def color_adjust_land(color, elevation):
    blue = min(255, int(255-elevation))
    red = min(255, int(255-elevation))
    green = min(255, int(255-elevation))
    return rgb_to_hex((red, green, blue ))
