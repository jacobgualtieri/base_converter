# Global Variables
binaryLookupTable = {
    "0": "0000", "1": "0001", "2": "0010", "3": "0011",
    "4": "0100", "5": "0101", "6": "0110", "7": "0100",
    "8": "1000", "9": "1001", "a": "1010", "b": "1011",
    "c": "1100", "d": "1101", "e": "1110", "f": "1111",
    "A": "1010", "B": "1011", "C": "1100", "D": "1101",
    "E": "1110", "F": "1111"}

hexLookupTable = {
    "0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4",
    "0101": "5", "0110": "6", "0111": "7", "1000": "8",
    "1001": "9", "1010": "A", "1011": "B", "1100": "C",
    "1101": "D", "1110": "E", "1111": "F"}

MODE_OPTIONS = "1: Binary -> Decimal\n2: Decimal -> Binary\n3: Hex -> Decimal\n" \
               "4: Decimal -> Hex\n5: Hex -> Binary\n6: Binary -> Hex"

def chooseMode(num):
    global MODE_OPTIONS
    print(num)
    print(MODE_OPTIONS)
    choiceList = ['1', '2', '3', '4', '5', '6']
    choice = input("Which mode would you like? ")
    if choice not in choiceList:
        print("Invalid Input...")
        return None
    else:
        choice = int(choice)
        if choice == 1:
            return binaryToDecimal(num)
        elif choice == 2:
            return decimalToBinary(int(num))
        elif choice == 3:
            return hexToDecimal(num)
        elif choice == 4:
            return decimalToHex(int(num))
        elif choice == 5:
            return hexToBinary(num)
        else: return binaryToHex(num)


def zeroExtend(binaryString):
    numZeros = 4 - len(binaryString)
    for i in range(numZeros):
        binaryString = "0" + binaryString
    return binaryString


def binaryToDecimal(binary_str):
    reversed_str = binary_str[::-1]
    decimal_value = 0
    for i in range(len(reversed_str)):
        if reversed_str[i] == '1':
            decimal_value += 2 ** i
    return decimal_value


def decimalToBinary(number):
    binaryString = ''
    while number >= 1:
        binaryString = binaryString + str(number % 2)
        number = number // 2
    return binaryString[::-1]


def hexToDecimal(hexString):
    global binaryLookupTable
    binaryString = ""
    for digit in hexString:
        binaryString += hex_digit_dict[digit]
    return binary_to_decimal(binaryString)


def decimalToHex(number):
    return binaryToHex(decimalToBinary(number))


def hexToBinary(hexString):
    binaryString = ''
    for digit in hexString:
        substring = binaryLookupTable[digit]
        binaryString += substring
    return binaryString


def binaryToHex(binaryString):
    global hexLookupTable
    index = 0
    substring = ''
    hexString = ''
    binaryString = binaryString[::-1]
    while index < len(binaryString):
        substring = binaryString[index] + substring
        if len(substring) >= 4:
            if substring != '':
                hexString = hexLookupTable[substring] + hexString
            else:
                pass
            substring = ''
        elif len(substring) < 4 and index == len(binaryString) - 1:
            extendedStr = zeroExtend(substring)
            if extendedStr != '':
                hexString = hexLookupTable[extendedStr] + hexString
            else:
                pass
        index += 1
    return hexString


# Main function used for testing
if __name__ == "__main__":
    inputValue = 32
    result = chooseMode(inputValue)
    print(result)
