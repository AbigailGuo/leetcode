# https://leetcode.com/problems/maximum-subarray/
def maxSubArray(nums):
    max_result = result = nums[0]
    for i in range(1, len(nums)):
        result =  max(nums[i], nums[i]+result)
        if max_result<result:
            max_result = result
    return max_result

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
