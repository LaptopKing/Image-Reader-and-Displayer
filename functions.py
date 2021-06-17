pyautogui = ""
try:
    import pyautogui
except Exception as e:
    pass

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

def ScaleToSmall(have_display):
    if (have_display):
        for g in range(12):
            pyautogui.hotkey('ctrl', '-')
    else:
        pass

def ScaleToOriginal(have_display):
    if (have_display):
        pyautogui.hotkey('ctrl', '0')
    else:
        pass

def ImageSize(image, attempts):
    a,b = image.size
    image = image.resize((a, b // 2), resample=0, box=None)
    for a in range(attempts):
        a,b = image.size
        image = image.resize((a // 2, b // 2), resample=0, box=None)

    return image

def Help():
    print ("\n|*************|")
    print ("|* Help Menu *|")
    print ("|*************|")
    print ("ˇ             ˇ")
    print ("For this help menu enter '--help' after the program call.\n\nUsage of program:\n\tThe program takes two arguments:\n\t\t1. Image filename\n\t\t2. Downscaling value [eg.: 2]\n\nExample of program usage:\n\t python3 reader.py test.jpeg 2")
