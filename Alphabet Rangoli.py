import string
def print_rangoli(size):
    alpha = string.ascii_lowercase

    lines = []
    for i in range(size):
        left = alpha[size-1:i:-1]   
        center = alpha[i]          
        right = alpha[i+1:size]    
        full = '-'.join(left + center + right)
        line = full.center(4 * size - 3, '-')  
        lines.append(line)
    print('\n'.join(lines[::-1] + lines[1:]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)