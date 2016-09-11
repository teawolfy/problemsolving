def is_prime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False

count = 1
pf = 0

for i in range(3,775146): #using the square root of the target number
    if 600851475143 % i == 0:
        f = int(600851475143/i)
        if is_prime(i) == True and i > pf:
            pf = i
        if is_prime(f) == True and f > pf:
            pf = f
print(pf)