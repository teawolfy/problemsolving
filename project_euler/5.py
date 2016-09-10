smalls = 0
count = 0
while smalls == 0:
    count += 1
    for i in range(2, 20):
        if count % i != 0:
            break
    else:
        smalls = count
print(smalls)