from math import sqrt

def count_factors(num):
    count = 0
    for i in range(1, (int(sqrt(num) + 1))):
        if num % i == 0:
            count += 2
    return count

factor_count = 0
tri = 1
add = 2

while factor_count <= 500:
    tri += add
    factor_count = count_factors(tri)
    add += 1
print(tri)