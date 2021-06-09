import numpy as np
from time import sleep
import ColorANSIRGB

color = ColorANSIRGB

X = 960
Y = 960

image = open("image.jpg")

img = np.fromfile(image, dtype=np.uint8, count = X * Y)

def findNum(img):
    size = img.sizenums = []
    for i in range (size):
        try:
            if (size % i == 0):
                nums.append(i)
        except Exception as e:
            pass

    for k in range (len(nums) // 2):
        nums.remove(max(nums))

    return max(nums)
num = findNum(img)

img.shape = (img.size // num, num)

for i in img:
    for k in i:
        print (k, end=' ')
        sleep (0.75)
    sleep(1)
    print()