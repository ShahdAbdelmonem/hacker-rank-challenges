from collections import Counter

x = int(input())
sizes = list(map(int, input().split()))
n = int(input())

available = Counter(sizes)
money = 0

for i in range(n):
    size, price = map(int, input().split())
    if available[size]:
        money += price
        available[size] -= 1

print(money)
