def rotate_list(nums, k):
    if not nums:                    # empty list
        return []
    k = k % len(nums)               # k may be bigger than the list: a full rotation changes nothing
    return nums[-k:] + nums[:-k]    # last k items first, then everything before them