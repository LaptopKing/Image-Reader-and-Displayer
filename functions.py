def DecToHex(decimal):
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ''

    while (decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16
    
    if (len(hexadecimal) == 1):
        hexadecimal += hexadecimal

    return hexadecimal  * 3

def FindNum(img):
    return img.size // 2

def ImgRes(image):
    print(image.read(100))
"""
image = open('test.jpg', 'rb')

ImgRes(image)
"""