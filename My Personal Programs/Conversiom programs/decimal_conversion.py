num=int(input("Enter the number:"))

def binary(n):
    binary_sum=0
    i=0
    while n!=0:
        binary_sum = binary_sum + (n%2)*(10**i)
        n = n // 2
        i = i + 1
    return binary_sum

def octal(n):
    octal_sum=0
    i=0
    while n!=0:
        octal_sum = octal_sum + (n%8)*(10**i)
        n = n // 8
        i = i + 1
    return octal_sum

def hexadecimal(n):
    hexadecimal_string=""
    hex_table = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    while n!=0:
        hexadecimal_string = hex_table[n%16] + hexadecimal_string
        n = n // 16
    return hexadecimal_string
    


if num<0:
    print("Please! Enter the whole number.")
elif num==0:
    print(f"Binary of {num}: 0b{0}")
    print(f"Octal of {num}: 0o{0}")
    print(f"Hexadecimal of {num}: 0x{0}")
else:
    print(f"Binary of {num}: 0b{binary(num)}")
    print(f"Octal of {num}: 0o{octal(num)}")
    print(f"Hexadecimal of {num}: 0x{hexadecimal(num)}")