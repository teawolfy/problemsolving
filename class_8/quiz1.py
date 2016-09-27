from math import sqrt

def crazy_about_9(a, b):
    if a == 9 or b == 9:
        return True
    elif a + b == 9 or abs(a-b) == 9 or abs(b-a) == 9:
        return True

print(crazy_about_9(2, 9))
print(crazy_about_9(4, 5))
print(crazy_about_9(3, 8))

def leap_year(i):
    if i % 400 == 0:
        return True
    elif i % 100 == 0:
        return False
    elif i % 4 == 0:
        return True
    else:
        return False

print(leap_year(1900))
print(leap_year(2016))
print(leap_year(2017))
print(leap_year(2000))

def sum_squares(i):
    sum = 0
    for n in range(1,i+1):
        if sqrt(n) / int(sqrt(n)) == 1:
            sum += n
            #print(n)
    return sum

def sumsquares(i):
    sum = 0
    for n in range(1, int(sqrt(i))+1):
        sum += n**2
    return sum

print(sum_squares(1))
print(sum_squares(100))
