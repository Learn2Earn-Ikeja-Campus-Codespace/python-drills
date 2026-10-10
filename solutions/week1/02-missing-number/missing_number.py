def find_missing(nums):
    for i in range(1, len(nums)):       # starts at 1 so nums[i - 1] always exists
        if nums[i] - nums[i-1] != 1:
            return nums[i] - 1          # the number right after the last good one