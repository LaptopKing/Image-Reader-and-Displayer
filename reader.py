import numpy as np
from time import sleep
import ColorANSIRGB
import sys

image = ""

try:
    image = open(str(sys.argv[1]))
except Exception as e:
    print (e)
    print ("[-] Failed running the program!\n[*] Probably there is no image what you have given or you did not give a full image name!")
    exit()

color = ColorANSIRGB

image = open("image.jpg")

img = np.fromfile(image, dtype=np.uint8, count = X * Y)

def DecToHex(decimal):
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ''

    while (decimal > 0):
        remainder = deciaml % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    
    return hexadecimal

def FindNum(img):
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

num = FindNum(img)

img.shape = (img.size // num, num)

for i in img:
    for k in i:
        print (DecToHex(k), end=' ')
        sleep (0.75)
    sleep(1)
    print()