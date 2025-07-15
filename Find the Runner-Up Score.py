if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorting= sorted(set(arr))
    print(sorting[-2])