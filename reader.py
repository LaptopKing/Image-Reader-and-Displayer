import numpy as np
from time import sleep
import ColorANSIRGB
import sys
from functions import *

image = ""

try:
    image = open(str(sys.argv[1]))
except Exception as e:
    print (e)
    print ("\n[-] Failed running the program!\n[*] Probably there is no image what you have given or you did not give a full image name!")
    exit()

color = ColorANSIRGB

img = np.fromfile(image, dtype=np.uint8, count = X * Y)

num = FindNum(img)

img.shape = (img.size // num, num)

for i in img:
    for k in i:
        print (DecToHex(k), end=' ')
        sleep (0.75)
    sleep(1)
    print()