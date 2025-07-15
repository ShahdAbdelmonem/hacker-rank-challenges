def print_h(n):
    letter = 'H'
    for i in range(n):
        left = (letter * i).rjust(n - 1)
        right = (letter * i).ljust(n - 1)
        print(left + letter + right)
    for i in range(n + 1):
        print((letter * n).center(n * 2) + (letter * n).center(n * 6))
    for i in range((n + 1) // 2):
        print((letter * n * 5).center(n * 6))
    for i in range(n + 1):
        print((letter * n).center(n * 2) + (letter * n).center(n * 6))
    for i in range(n):
        left = (letter * (n - i - 1)).rjust(n)
        right = (letter * (n - i - 1)).ljust(n)
        print((left + letter + right).rjust(n * 6))
if __name__ == '__main__':
    thickness = int(input())
    print_h(thickness)