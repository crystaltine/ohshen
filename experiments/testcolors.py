import stringcolor, colorsys


test_color = colorsys.hsv_to_rgb(0, 0, 0)
    
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

test_color = tuple([int(val * 255) for val in test_color])
print(get_color_escape(*test_color, background=False) + "test text")
print(get_color_escape(0, 0, 60, background=False) + "test text")