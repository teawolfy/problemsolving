from math import sqrt
answer = 0

for a in range(1,1000):
    for b in range(a,1000):
        c = sqrt(a**2 + b**2)
        if c / int(c) == 1 and a + b + c == 1000:
            answer = a * b * c
            break
        b += 1
    a += 1
print(answer)
    