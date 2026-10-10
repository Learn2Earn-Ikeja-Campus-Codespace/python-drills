def intersection(a, b):
    result = []                              # new list, neither input is modified
    for x in a:
        if x in b and x not in result:       # in both lists, and not added before (no duplicates)
            result.append(x)
    return result