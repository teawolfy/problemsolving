from math import sqrt

i = float(input('Please input an integer to be factored '))

def my_factor(x):
    factor_list = []
    x = int(x)
    for num in range(1, int(sqrt(x)+1)):
        if x % num == 0:
            factor_list.append(num)
            factor_list.append(int(x / num))
    return factor_list

print(my_factor(i))
