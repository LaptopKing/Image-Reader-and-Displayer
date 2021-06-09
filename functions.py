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