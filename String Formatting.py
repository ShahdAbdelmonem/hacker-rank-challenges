def print_formatted(number):
    Width = len(bin(number)[2:])
    for i in range(1, number + 1):
        Decimal = str(i).rjust(Width)
        Octal = oct(i)[2:].rjust(Width)
        Hexadecimal = hex(i)[2:].upper().rjust(Width)
        Binary = bin(i)[2:].rjust(Width)
        print(Decimal, Octal, Hexadecimal, Binary)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)