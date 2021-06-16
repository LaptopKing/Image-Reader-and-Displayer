def DecToHex(nums):
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    temp_hexadecimal = ''
    hexadecimal = ''

    for decimal in nums:
        temp_hexadecimal = ''
        if (decimal == 255):
            temp_hexadecimal += 'FF'
            hexadecimal += temp_hexadecimal
        elif (decimal == 0):
            temp_hexadecimal += '00'
            hexadecimal += temp_hexadecimal
        else:
            while (decimal > 0):
                remainder = decimal % 16
                temp_hexadecimal = conversion_table[remainder] + temp_hexadecimal
                decimal = decimal // 16
        
            if (len(temp_hexadecimal) == 1):
                temp_hexadecimal += temp_hexadecimal
                hexadecimal += temp_hexadecimal
            else:
                hexadecimal += temp_hexadecimal

    if (len(hexadecimal) == 8):
        return hexadecimal.replace(temp_hexadecimal, '')
    else:
        return hexadecimal

def FindNum(img):
    return img.size // 2

def ImgRes(image):
    print(image.read(100))
"""
image = open('test.jpg', 'rb')

ImgRes(image)
"""