hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    dec=0
    
    for x in hexNum:
        if x in hexNumbers:
            dec=dec*16+hexNumbers.get(x)
        else:
            return None
    return dec

print(hexToDec('3C0'))
print(hexToDec('3C0Z'))