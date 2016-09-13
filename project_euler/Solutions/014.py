def chain_length(num):
    length = 1
    while num > 1:
        length += 1
        if num % 2 == 0:
            num = num/2
        else:
            num = 3 * num + 1
    return length

answer = 0
top_length = 0
for i in range(1,1000000):
    if chain_length(i) > top_length:
        top_length = chain_length(i)
        answer = i
print(answer)