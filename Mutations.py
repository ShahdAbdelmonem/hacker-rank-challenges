def mutate_string(string, position, character):
    liist = list(string)
    liist[position] = character
    return ''.join(liist)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)