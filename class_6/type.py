def type_check(a, b):
    if type(a) == str or type(b) == str:
        return 'string involved'
    else:
        if a == b:
            return 'equal'
        if a > b:
            return 'bigger'
        else:
            return 'smaller'
print(type_check(5,5))