import numpy as np
import re
import itertools
from time import sleep
import sys
from functions import *

image = ""

try:
    image = open(str(sys.argv[1]), 'rb')
except Exception as e:
    print (e)
    print ("\n[-] Failed running the program!\n[*] Probably there is no image what you have given or you did not give a full image name!")
    exit()

class ColorANSIRGB:
    def __init__(self):

        self.ESC, self.RESET, self.STYLE, self.END = "\033", "[0", "[", "m"
        self.FOREGROUND, self.BACKGROUND = "[38;5;", "[48;5;"
        self.hex_prefix, self.hex_hash = '0x', '#'
        self.lo_8_colors = ['000000', '800000', '008000', '808000', '000080', '800080', '008080', 'c0c0c0']
        self.hi_8_colors = ['808080', 'ff0000', '00ff00', 'ffff00', '0000ff', 'ff00ff', '00ffff', 'ffffff']
        self.increments = (0x00, 0x5f, 0x87, 0xaf, 0xd7, 0xff)
        self.color_matrix_increments = range(95, 256, 40)

        self.styles_list = ['normal', 'bold', 'dim', 'italic', 'underline', 'blink', 'reverse']
        self.style_values = [value for value in range(8) if value != 6]
        self.styles = dict(zip(self.styles_list, self.style_values))

        self.basic_16 = self.lo_8_colors + self.hi_8_colors
        self.strip_regex = r'(..)(..)(..)'

        self.color_cube = self.color_cube_matrix()
        self.string_color_cube = self.string_color_cube_matrix()
        self.ansi_256 = self.ansi_256_dict()

    def strip_hash(self, rgb_string):
        return rgb_string.lstrip(self.hex_hash) if rgb_string.startswith(self.hex_hash) else rgb_string

    def reset(self):
        return "%s%s%s" % (self.ESC, self.RESET, self.END)

    def style(self, text_style=None):
        _pre = "%s%s" % (self.ESC, self.STYLE)
        if not text_style and text_style != 0:
            return ""
        if isinstance(text_style, int):
            return "%s%s%s" % (_pre, text_style, self.END) if text_style in self.style_values else ""
        elif isinstance(text_style, str) and text_style in self.styles_list:
            try:
                return "%s%s%s" % (_pre, self.styles[text_style], self.END)
            except IndexError:
                return ""
        else:
            return ""

    def color_cube_matrix(self):
        hex_list = ["00"]
        for value in self.color_matrix_increments:
            hex_list.append(hex(value).lstrip(self.hex_prefix))
        rgb_hex_lists = [hex_list] * 3
        return list(itertools.product(*rgb_hex_lists))

    def string_color_cube_matrix(self):
        color_cube_values = list()
        for entry in self.color_cube:
            color_cube_values.append(''.join([hex_value for hex_value in entry]))
        return color_cube_values

    def ansi_16_dict(self):
        ansi_16_colors = dict()
        for index_value in range(16):
            ansi_16_colors.update({str(index_value): self.basic_16[index_value]})
        return ansi_16_colors

    def ansi_216_dict(self):
        ansi_216_colors = dict()
        basic_216 = self.string_color_cube
        for index_value in range(216):
            ansi_216_colors.update({str(index_value + 16): basic_216[index_value]})
        return ansi_216_colors

    def ansi_256_dict(self):
        return {**self.ansi_16_dict(), **self.ansi_216_dict()}

    def closest_rgb(self, rgb_value_string):
        stripped_rgb = re.split(self.strip_regex, self.strip_hash(rgb_value_string))[1:4]
        stripped_rgb = [int(value, 16) for value in stripped_rgb]
        closest_r_g_b = list()
        for _color in stripped_rgb:
            _index = 0
            while _index < len(self.increments) - 1:
                smaller, bigger = self.increments[_index], self.increments[_index + 1]
                if smaller <= _color <= bigger:
                    _smaller, _bigger = abs(smaller - _color), abs(bigger - _color)
                    closest = smaller if _smaller < _bigger else bigger
                    closest_r_g_b.append(closest)
                    break
                _index += 1
        closest_r_g_b = ''.join([('%02.x' % _idx) for _idx in closest_r_g_b])
        return closest_r_g_b

    def closest_ansi(self, rgb_value_string):
        ansi_viable_rgb = self.closest_rgb(rgb_value_string)
        key = next(key for key, value in self.ansi_256.items() if value == ansi_viable_rgb)
        return key

    def rgb_to_ansi(self, fg_rgb, bg_rgb=None):
        fg_rgb = self.closest_ansi(fg_rgb)
        _fg = "%s%s%s%s" % (self.ESC, self.FOREGROUND, fg_rgb, self.END)
        if bg_rgb:
            bg_rgb = self.closest_ansi(bg_rgb)
            _bg = "%s%s%s%s" % (self.ESC, self.BACKGROUND, bg_rgb, self.END)
            return "%s%s" % (_bg, _fg)
        return _fg

    def ansi_to_rgb(self, ansi_value):
        return self.ansi_256[str(ansi_value)]

    def rgb(self, fg, bg=None, style=None):
        ansi_string = self.rgb_to_ansi(fg, bg)
        return self.reset() + self.style(style) + ansi_string

    def ansi(self, ansi_fg, ansi_bg=None, style=None):
        style = self.style(style) if style else ""
        _fg = "%s%s%s%s" % (self.ESC, self.FOREGROUND, str(ansi_fg), self.END)
        if ansi_bg:
            _bg = "%s%s%s%s" % (self.ESC, self.BACKGROUND, str(ansi_bg), self.END)
            return self.reset() + style + "%s%s" % (_bg, _fg)
        return self.reset() + style + _fg

color = ColorANSIRGB()
reset = color.reset()


X = 713
Y = 734

img = np.fromfile(image, dtype=np.uint8, count = X * Y)

img.shape = (img.size // Y, Y)

for j in img:
    for k in j:
        if (DecToHex(k) == ""):
            print(color.rgb("00000000", "00000000"), end=" ")
        else:
            print(color.rgb(DecToHex(k), DecToHex(k)), end=" ")
    print()

"""
for i in range(len(img_hex)):
    if (img_hex[i] == ""):
        print (color.rgb("00000000", "00000000"))
    elif (img_hex[i] == ""):
        print (color.rgb("FFFFFFFF", "FFFFFFFF"), end=" ")
    else:
        print (color.rgb(img_hex[i], img_hex[i]), end=" ")
"""