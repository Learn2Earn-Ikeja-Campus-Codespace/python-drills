def remove_duplicates(nums):
    result = []                 # new list, so the input is never modified
    for n in nums:
        if n not in result:     # only the first occurence gets through
            result.append(n)
    return result