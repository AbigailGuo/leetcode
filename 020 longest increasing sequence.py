# https://leetcode.com/problems/longest-increasing-subsequence/

# 最基本的dp方法 
def lengthOfLIS(nums):
    dp =[1 for _ in range(0, len(nums))]
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j]>nums[i]:
                dp[i] =  max(dp[i], dp[j]+1)
    return max(dp)

print(lengthOfLIS([10,9,2,5,3,7,101,18]))