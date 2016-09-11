#using Sieve of Eratosthenes instead of brute force prime checking every number

primes = [True] * 2000000
primes[0] = None
primes[1] = None
sum = 0

for index, value in enumerate(primes):
    if value == True:
        primes[index*2::index] = [False] * ((1999999 // index) - 1)
        sum += index
print(sum)