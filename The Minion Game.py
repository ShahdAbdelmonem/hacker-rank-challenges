def minion_game(string):
    vowels = 'AEIOU'
    kevin_points = 0
    stuart_points = 0
    n = len(s)

    for i in range(n):
        if s[i] in vowels:
            kevin_points += n - i
        else:
            stuart_points += n - i

    if kevin_points > stuart_points:
        print("Kevin", kevin_points)
    elif stuart_points > kevin_points:
        print("Stuart", stuart_points)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)