def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list

    my_list: an ordered list of numbers from smallest to largest

    x: a number

    returns the index of x if x is in my_list, None if not.
    '''
    my_list.sort()
    beg = 0
    end = len(my_list)
    index = 0
    while end - beg > 0:
        if x == my_list[(beg + end) // 2]:
            return (beg + end) // 2
        elif x < my_list[(beg + end) // 2]:
            end = (beg + end) // 2
        else:
            beg = ((beg + end) // 2) + 1
        #print(beg, end)
    return None
    pass


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()
print(test_list)

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None