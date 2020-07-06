# https://leetcode.com/problems/minimum-size-subarray-sum/
def minSubArrayLen( s, nums):
    if sum(nums)<s:
            return 0
    sum_ = 0
    right = 0
    left = 0
    min_length = len(nums)
    while right<len(nums):
        while sum_ < s and right<len(nums):
            sum_ += nums[right]
            right += 1
        while sum_>=s:
            min_length = min(min_length, right-left)
            sum_ -= nums[left]
            left += 1
    print(min_length)
    return min_length
            

minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12])