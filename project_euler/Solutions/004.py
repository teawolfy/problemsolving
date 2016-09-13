def is_palindrome(num):
    if str(num) == (str(num)[::-1]):
        return True
    else:
        return False

pal = 0
for x in range(100, 999):
    for y in range(x + 1, 999):
        product = x * y
        if product > pal and is_palindrome(product) == True:
            pal = product
print(pal)