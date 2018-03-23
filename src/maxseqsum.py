ef maxseqsum(nums):
    this_sum = max_sum = 0
    for i in range(len(nums)):
        this_sum += nums[i]
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum
