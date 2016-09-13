fib = 2
prev = 2
prevprev = 1
new = 0
while new < 4000000:
    new = prev + prevprev
    prevprev = prev
    prev = new
    if new % 2 == 0:
        fib += new
print(fib)