if __name__ == '__main__':
    student= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])

    scores = [s[1] for s in student]
    sscores = sorted(set(scores))
    second_score = sscores[1]
    result = [s[0] for s in student if s[1] == second_score]
    result.sort()

    for name in result:
        print(name)
