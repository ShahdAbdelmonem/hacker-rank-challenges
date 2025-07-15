import cmath

z = complex(input())
r = abs(z)
angle = cmath.phase(z)

print(r)
print(angle)