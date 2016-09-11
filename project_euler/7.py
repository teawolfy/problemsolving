#using Sieve of Eratosthenes instead of brute force prime checking every number

primes = [True] * 200000 #picked some number I expected to be larger than 10,001st prime
primes[0] = None
primes[1] = None
count = 0
answer = 0

for index, value in enumerate(primes):
    if value == True:
        primes[index*2::index] = [False] * ((199999 // index) - 1)
        count += 1
    if count == 10001:
        answer = index
        break
print(answer)
