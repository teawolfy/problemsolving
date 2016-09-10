sum = 0
sumsquare = 0
for i in range(1, 101):
    sumsquare += i**2
    sum += i
squaresum = sum**2
print(squaresum - sumsquare)